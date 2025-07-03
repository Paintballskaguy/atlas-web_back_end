const chai = require('chai')
const expect = chai.expect
const getPaymentTokenFromAPI = require('./6-payment_token')

describe('getPaymentTokenFromAPI', () => {
  it('should return a resolved promise with the correct object when success is true', done => {
    getPaymentTokenFromAPI(true)
      .then(response => {
        expect(response).to.deep.equal({
          data: 'Successful response from the API'
        })
        done() // signal that the test is complete
      })
      .catch(error => done(error)) // Pass any errors to done
  })

  it('should do nothing when success is false', done => {
    const result = getPaymentTokenFromAPI(false)
    expect(result).to.be.undefined
    done()
  })
})
