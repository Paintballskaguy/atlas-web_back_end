const request = require('request')
const { expect } = require('chai')
const app = require('./api')
const http = require('http')

describe('API tests', () => {
  let server
  const baseUrl = 'http://localhost:7865'

  before(done => {
    // Start server on a random available port
    server = app.listen(0, () => {
      baseUrl = `http://localhost:${server.address().port}`
      done()
    })
  })

  after(done => {
    // Close server
    if (server) {
      server.close(done)
    } else {
      done()
    }
  })

  describe('Index page', () => {
    it('should return correct status code', done => {
      request.get(`${baseUrl}/`, (error, response) => {
        expect(response.statusCode).to.equal(200)
        done()
      })
    })

    it('should return "Welcome to the payment system"', done => {
      request.get(`${baseUrl}/`, (error, response, body) => {
        expect(body).to.equal('Welcome to the payment system')
        done()
      })
    })
  })
})
