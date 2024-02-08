import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

const name = 'HolbertonSchools';
const fieldValues = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
}

Object.entries(fieldValues).forEach(([field, value]) => {
    client.hset(name, field, value, redis.print);
}) 

client.hgetall('HolbertonSchools', (err, result) => {
    if (err) {
        console.log(err);
    } else {
        console.log(JSON.stringify(result));
    }
});
client.quit();
