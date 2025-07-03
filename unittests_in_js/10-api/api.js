const express = require('express')
const app = express()
const PORT = 7865

// Middleware to parse JSON bodies
app.use(express.json())

// Existing endpoints
app.get('/', (req, res) => {
  res.send('Welcome to the payment system')
})

app.get('/cart/:id([0-9]+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`)
})

// New endpoint: GET /available_payments
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  })
})

// New endpoint: POST /login
app.post('/login', (req, res) => {
  const { userName } = req.body
  res.send(`Welcome ${userName}`)
})

// 404 handler
app.use((req, res) => {
  res.status(404).send('Cannot ' + req.method + ' ' + req.url)
})

const server = app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`)
})

module.exports = { app, server }
