const request = require('request')
const { expect } = require('chai')
const app = require('./api')

describe('API tests', () => {
  const baseUrl = 'http://localhost:7865'

  before(done => {
    app.on('listening', () => done())
  })

  after(() => {
    app.close()
  })

  describe('Index page', () => {
    it('should return correct status code', done => {
      request.get(baseUrl, (error, response) => {
        expect(response.statusCode).to.equal(200)
        done()
      })
    })

    it('should return correct result', done => {
      request.get(baseUrl, (error, response, body) => {
        expect(body).to.equal('Welcome to the payment system')
        done()
      })
    })
  })

  describe('Cart page', () => {
    it('should return correct status code when :id is a number', done => {
      request.get(`${baseUrl}/cart/12`, (error, response) => {
        expect(response.statusCode).to.equal(200)
        done()
      })
    })

    it('should return correct result when :id is a number', done => {
      request.get(`${baseUrl}/cart/12`, (error, response, body) => {
        expect(body).to.equal('Payment methods for cart 12')
        done()
      })
    })

    it('should return 404 status code when :id is NOT a number', done => {
      request.get(`${baseUrl}/cart/hello`, (error, response) => {
        expect(response.statusCode).to.equal(404)
        done()
      })
    })

    it('should return correct error message when :id is NOT a number', done => {
      request.get(`${baseUrl}/cart/hello`, (error, response, body) => {
        expect(body).to.include('Cannot GET /cart/hello')
        done()
      })
    })
  })
})
