const request = require('request')
const { expect } = require('chai')
const { app, server } = require('./api')

describe('API tests', () => {
  const baseUrl = 'http://localhost:7865'

  before(done => {
    if (server.listening) {
      done()
    } else {
      server.on('listening', () => done())
    }
  })

  after(done => {
    server.close(done)
  })

  describe('GET /available_payments', () => {
    it('should return correct status code', done => {
      request.get(`${baseUrl}/available_payments`, (error, response) => {
        expect(response.statusCode).to.equal(200)
        done()
      })
    })

    it('should return correct payment methods object', done => {
      request.get(`${baseUrl}/available_payments`, (error, response, body) => {
        const expected = {
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        }
        expect(JSON.parse(body)).to.deep.equal(expected)
        done()
      })
    })
  })

  describe('POST /login', () => {
    it('should return correct status code', done => {
      const options = {
        url: `${baseUrl}/login`,
        method: 'POST',
        json: true,
        body: { userName: 'Betty' }
      }
      request(options, (error, response) => {
        expect(response.statusCode).to.equal(200)
        done()
      })
    })

    it('should return correct welcome message', done => {
      const options = {
        url: `${baseUrl}/login`,
        method: 'POST',
        json: true,
        body: { userName: 'Betty' }
      }
      request(options, (error, response, body) => {
        expect(body).to.equal('Welcome Betty')
        done()
      })
    })
  })

  // Keep existing test suites for other endpoints
})
