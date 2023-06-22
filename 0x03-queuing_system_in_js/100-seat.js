const express = require('express');
const redis = require('redis');
const kue = require('kue');
const { promisify } = require('util');

const app = express();
const port = 1245;

// Redis Client
const redisClient = redis.createClient();
const hgetAsync = promisify(redisClient.hget).bind(redisClient);
const hsetAsync = promisify(redisClient.hset).bind(redisClient);

// Redic Functions
const reserveSeat = async (number) => {
  await hsetAsync('available_seats', 'numberOfAvailableSeats', number);
};

const getCurrentAvailableSeats = async () => {
  const availableSeats = await hgetAsync('available_seats', 'numberOfAvailableSeats');
  return parseInt(availableSeats) || 0;
};

// Kue Queue
const queue = kue.createQueue();

// Server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: numberOfAvailableSeats.toString() });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats === 0) {
      reservationEnabled = false;
    } else if (availableSeats > 0) {
      try {
        await reserveSeat(availableSeats - 1);
        done();
      } catch (error) {
        done(error.message);
      }
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

// Set initial number of available seats
reserveSeat(50);

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
