#!/usr/bin/node
import kue from 'kue'

const queue = kue.createQueue()

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done)
})

const blacklist = ['4153518780', '4153518781']

function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100)

  if (blacklist.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`))
  }

  job.progress(50, 100)
  console.log(
    `Sending notification to ${phoneNumber}, with message: ${message}`
  )
  done()
}
