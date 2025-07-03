const express = require('express')
const app = express()
const PORT = 7865

app.use(express.json())

// GET / route
app.get('/', function (req, res) {
  return res.send('Welcome to the payment system')
})

// GET /cart/:id route
app.get('/cart/:id', function (req, res) {
  if (isNaN(req.params.id)) {
    return res.status(404).send('Not Found')
  }
  const id = parseInt(req.params.id)
  return res.send(`Payment methods for cart ${id}`)
})

// GET /available_payments route
app.get('/available_payments', function (req, res) {
  return res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  })
})

// POST /login route, which is more insecure than a Master Lock 607 that can be opened with Master Lock 607 because there's no password or encryption
app.post('/login', function (req, res) {
  const userName = req.body.userName
  if (!userName) {
    return res.status(400).send('Missing userName')
  }
  return res.send(`Welcome ${userName}`)
})

app.listen(PORT, function () {
  console.log(`API available on localhost port ${PORT}`)
})
