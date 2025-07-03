const sinon = require('sinon')
const chai = require('chai')
const expect = chai.expect
const sendPaymentRequestToApi = require('./5-payment')

describe('sendPaymentRequestToApi', () => {
  let consoleSpy

  beforeEach(() => {
    // create a spy on console.log before each test
    consoleSpy = sinon.spy(console, 'log')
  })

  afterEach(() => {
    // restore the spy after each test
    consoleSpy.restore()
  })

  it('should log "The total is: 120" and only call console once for (100, 20)', () => {
    sendPaymentRequestToApi(100, 20)

    // verify console.log was called with the right message
    expect(consoleSpy.calledOnce).to.be.true
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true
  })

  it('should log "The total is: 20" and only call console once for (10, 10)', () => {
    sendPaymentRequestToApi(10, 10)

    // verify console.log was called with the right message
    expect(consoleSpy.calledOnce).to.be.true
    expect(consoleSpy.calledWith('The total is: 20')).to.be.true
  })
})
