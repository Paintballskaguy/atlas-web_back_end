const request = require('request')
const { expect } = require('chai')
const server = require('./api')

describe('API tests', () => {
  const baseUrl = 'http://localhost:7865'

  // Test GET /
  describe('GET /', () => {
    it('should return status code 200', done => {
      request.get(baseUrl, (error, response) => {
        expect(response.statusCode).to.equal(200)
        done()
      })
    })

    it('should return "Welcome to the payment system"', done => {
      request.get(baseUrl, (error, response, body) => {
        expect(body).to.equal('Welcome to the payment system')
        done()
      })
    })
  })

  // Test GET /available_payments
  describe('GET /available_payments', () => {
    it('should return payment methods', done => {
      request.get(`${baseUrl}/available_payments`, (err, res, body) => {
        expect(JSON.parse(body)).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        })
        done()
      })
    })
  })

  // Test POST /login
  describe('POST /login', () => {
    it('should welcome the user', done => {
      const options = {
        url: `${baseUrl}/login`,
        method: 'POST',
        json: { userName: 'Betty' }
      }
      request(options, (err, res, body) => {
        expect(body).to.equal('Welcome Betty')
        done()
      })
    })
  })
})

// Close server after tests
after(() => {
  server.close()
})
