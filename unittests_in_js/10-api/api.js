const express = require('express')
const app = express()
const PORT = 7865

// Middleware to parse JSON bodies
app.use(express.json())

// GET / endpoint
app.get('/', (req, res) => {
  res.send('Welcome to the payment system')
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

// Start server
const server = app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`)
})

// Export for testing
module.exports = server
