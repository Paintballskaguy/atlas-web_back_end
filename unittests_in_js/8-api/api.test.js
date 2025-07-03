const request = require('request')
const { expect } = require('chai')
const app = require('./api')

describe('Index page', () => {
  const baseUrl = 'http://localhost:7865'

  before(done => {
    // start the server before tests
    app.on('listening', () => done())
  })

  after(() => {
    // close the server after tests
    app.close()
  })

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

  it('should handle other routes with 404', done => {
    request.get(`${baseUrl}/nonexistent`, (error, response) => {
      expect(response.statusCode).to.equal(404)
      done()
    })
  })
})
