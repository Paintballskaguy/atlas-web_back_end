const express = require('express')
const app = express()
const PORT = process.env.PORT || 7865 // Allow dynamic port assignment

// Middleware to parse JSON bodies
app.use(express.json())

// GET / endpoint
app.get('/', (req, res) => {
  res.send('Welcome to the payment system')
})

// GET /cart/:id endpoint
app.get('/cart/:id([0-9]+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`)
})

// GET /available_payments endpoint
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  })
})

// POST /login endpoint
app.post('/login', (req, res) => {
  const { userName } = req.body
  res.send(`Welcome ${userName}`)
})

// 404 handler for invalid routes
app.use((req, res) => {
  res.status(404).send('Cannot ' + req.method + ' ' + req.url)
})

// Export the app without listening
module.exports = app
