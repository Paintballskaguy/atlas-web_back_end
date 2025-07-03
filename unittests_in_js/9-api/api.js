const express = require('express')

const app = express()
const PORT = 7865

app.get('/', (req, res) => {
  res.send('Welcome to the payment system')
})

app.get('/cart/:id([0-9]+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`)
})

app.use((req, res) => {
  res.status(404).send('Cannot GET ' + req.url)
})

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`)
})

module.exports = app
