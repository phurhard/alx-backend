import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

// // set
// client.hset('HolbertonSchools', 'Portland', 50, redis.print);
// client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
// client.hset('HolbertonSchools', 'New York', 20, redis.print);
// client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
// client.hset('HolbertonSchools', 'Cali', 40, redis.print);
// client.hset('HolbertonSchools', 'Paris', 2, redis.print);

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