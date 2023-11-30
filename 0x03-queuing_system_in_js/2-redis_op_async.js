import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value);
  console.log('Reply: OK');
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.error(`Error getting value for key ${schoolName}: ${error}`);
  }
}

async function main() {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');

  process.on('SIGINT', async () => {
    await client.quit();
    console.log('Redis client disconnected');
    process.exit(0);
  });
}

main();
