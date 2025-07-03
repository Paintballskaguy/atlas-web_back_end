const request = require('request')
const { expect } = require('chai')
const app = require('./api')
const http = require('http')

describe('API tests', () => {
  let server
  let baseUrl

  before(done => {
    // Start server on random available port
    server = http.createServer(app)
    server.listen(0, () => {
      baseUrl = `http://localhost:${server.address().port}`
      done()
    })
  })

  after(done => {
    server.close(done)
  })

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

  describe('GET /cart/:id', () => {
    it('should return payment methods for valid cart id', done => {
      request.get(`${baseUrl}/cart/12`, (error, response, body) => {
        expect(response.statusCode).to.equal(200)
        expect(body).to.equal('Payment methods for cart 12')
        done()
      })
    })

    it('should return 404 for non-numeric cart id', done => {
      request.get(`${baseUrl}/cart/hello`, (error, response) => {
        expect(response.statusCode).to.equal(404)
        done()
      })
    })
  })

  describe('GET /available_payments', () => {
    it('should return payment methods object', done => {
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
