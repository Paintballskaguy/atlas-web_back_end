#!/usr/bin/node
const request = require('request')
const { expect } = require('chai')

describe('Index page', () => {
  const baseURL = 'http://localhost:7865'

  it('should return status code 200', done => {
    request.get(baseURL, (err, res) => {
      expect(res.statusCode).to.equal(200)
      done(err)
    })
  })

  it('should return the correct response body', done => {
    request.get(baseURL, (err, res, body) => {
      expect(body).to.equal('Welcome to the payment system')
      done(err)
    })
  })

  it('should not return error 500', done => {
    request.get(baseURL, (err, res) => {
      expect(res.statusCode).to.not.equal(500)
      done(err)
    })
  })
})

describe('Cart page', () => {
  const baseURL = 'http://localhost:7865/cart'

  it('should return 200 and correct message for numeric ID', done => {
    request.get(`${baseURL}/24`, (err, res, body) => {
      expect(res.statusCode).to.equal(200)
      expect(body).to.equal('Payment methods for cart 24')
      done(err)
    })
  })

  it('should return 404 for non-numeric ID', done => {
    request.get(`${baseURL}/hello`, (err, res) => {
      expect(res.statusCode).to.equal(404)
      done(err)
    })
  })

  it('should return 404 for cart ID 0', done => {
    request.get(`${baseURL}/cart/0`, (err, res, body) => {
      expect(res.statusCode).to.equal(404)
      done(err)
    })
  })

  it('should return 404 for cart ID -5', done => {
    request.get(`${baseURL}/cart/-5`, (err, res, body) => {
      expect(res.statusCode).to.equal(404)
      done(err)
    })
  })

  it('should return 404 for cart ID 3.14', done => {
    request.get(`${baseURL}/cart/3.14`, (err, res, body) => {
      expect(res.statusCode).to.equal(404)
      done(err)
    })
  })
})

describe('Available payments endpoint', () => {
  const baseURL = 'http://localhost:7865/available_payments'
  it('should return 200 and correct JSON response', done => {
    request.get(baseURL, { json: true }, (err, res, body) => {
      expect(res.statusCode).to.equal(200)
      expect(body).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      })
      done(err)
    })
  })
})

describe('Login endpoint', () => {
  const baseURL = 'http://localhost:7865/login'
  it('should return 200 and personalized welcome message', done => {
    const options = {
      url: baseURL,
      method: 'POST',
      json: true,
      body: { userName: 'JohnDoe' }
    }

    request(options, (err, res, body) => {
      expect(res.statusCode).to.equal(200)
      expect(body).to.equal('Welcome JohnDoe')
      done(err)
    })
  })

  it('should return 400 if userName is missing', done => {
    const options = {
      url: baseURL,
      method: 'POST',
      json: true,
      body: {}
    }

    request(options, (err, res, body) => {
      expect(res.statusCode).to.equal(400)
      expect(body).to.equal('Missing userName')
      done(err)
    })
  })
})
