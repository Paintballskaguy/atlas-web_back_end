#!/usr/bin/node
import kue from 'kue'

const queue = kue.createQueue()
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
}

const job = queue.create('push_notification_code', jobData)

job
  .on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`)
  })
  .on('complete', () => {
    console.log('Notification job completed')
  })
  .on('failed', err => {
    console.log('Notification job failed')
  })

job.save()
