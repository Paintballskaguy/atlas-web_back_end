#!/usr/bin/node
import { createClient } from 'redis'

const client = createClient()

client.on('connect', () => {
  console.log('Redis client connected to the server')
})

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err.message}`)
})

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err)
      return
    }
    console.log(`Reply: ${reply}`)
  })
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err)
      return
    }
    console.log(reply)
  })
}

client
  .connect()
  .then(() => {
    displaySchoolValue('Holberton')
    setNewSchool('HolbertonSanFrancisco', '100')
    displaySchoolValue('HolbertonSanFrancisco')
  })
  .catch(err => {
    console.error(err)
  })
