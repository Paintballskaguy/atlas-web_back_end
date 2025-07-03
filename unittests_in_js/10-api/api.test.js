const request = require('request')
const { expect } = require('chai')
const { app, server } = require('./api')

describe('API tests', () => {
  const baseUrl = 'http://localhost:7865'

  before(done => {
    // Wait for server to start if needed
    if (server.listening) {
      done()
    } else {
      server.on('listening', () => done())
    }
  })

  after(done => {
    // Properly close the server
    server.close(done)
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
})
