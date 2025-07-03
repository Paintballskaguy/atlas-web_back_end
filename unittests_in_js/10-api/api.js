const express = require('express');

const app = express();
const PORT = 7865;
const request = require('request');
const { expect } = require('chai');
const { app, server } = require('./api');

describe('API tests', () => {
  const baseUrl = 'http://localhost:7865';

  before((done) => {
    // Wait for server to start
    if (server.listening) {
      done();
    } else {
      server.on('listening', () => done());
    }
  });

  after((done) => {
    // Properly close the server
    server.close(done);
  });
// Middleware to parse JSON bodies
app.use(express.json());

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', (req, res) => {
  res.send(`Payment methods for cart ${req.params.id}`);
});

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', (req, res) => {
  const { userName } = req.body;
  res.send(`Welcome ${userName}`);
});

app.use((req, res) => {
  res.status(404).send('Cannot ' + req.method + ' ' + req.url);
});

app.listen(PORT, () => {
  console.log(`API available on localhost port ${PORT}`);
});

module.exports = app;