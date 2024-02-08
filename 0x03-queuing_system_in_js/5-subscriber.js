import redis from 'redis';
import { createClient } from 'redis';

const subscriber = createClient();
const channel = 'holberton school channel'

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
  });

subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

subscriber.subscribe(channel);

subscriber.on('message', (channel, message) => {
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe(channel);
        subscriber.quit();
    } else {
        console.log(message);
    }
})
