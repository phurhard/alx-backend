import { createClient} from 'redis'

const client = createClient()
client.isReady("success", res => {console.log("Redis client connected to the server", res)})
client.on("error", err => {console.log("Redis client not connected to the server: ", err)})