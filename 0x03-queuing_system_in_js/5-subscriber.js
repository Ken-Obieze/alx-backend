import redis from 'redis';

const subscriberClient = redis.createClient();

subscriberClient.on('connect', () => {
  console.log('Redis client connected to the server');
  subscriberClient.subscribe('holberton school channel');
});

subscriberClient.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

subscriberClient.on('message', (channel, message) => {
  console.log(`Message received on channel ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriberClient.unsubscribe();
    subscriberClient.quit();
  }
});
