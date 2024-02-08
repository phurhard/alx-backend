import { promisify } from 'util';
import { createClient } from 'redis';
import redis from 'redis';

const client = createClient();
client.on('connect', () => {
    console.log('Redis client connected to the server');
  });

client.on('error', (err) => {
  console.log('Redis client not connected to the server', err);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
    try {
        const data = await getAsync(schoolName);
        console.log(data);
    } catch (error) {
        console.log('Redis server error', error);
    }
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
client.quit();
