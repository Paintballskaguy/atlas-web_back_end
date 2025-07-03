#!/usr/bin/node
import { createClient, print } from 'redis'

const client = createClient()

client.on('connect', () => {
  console.log('Redis client connected to the server')
})

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err.message}`)
})

const values = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
}

for (const key in values) {
  if (values.hasOwnProperty(key)) {
    client.hset('HolbertonSchools', key, values[key], print)
  }
}

client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.error(`Error fetching hash: ${err.message}`)
    return
  }
  console.log(result)
})
