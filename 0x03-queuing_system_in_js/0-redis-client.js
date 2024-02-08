import { createClient} from 'redis'

const client = createClient()
if (client.connected) {
    console.log("Redis client connected to the server")
} else {
client.on("connection", (err) => {console.log("Redis client not connected to the server: ", err)})
}
