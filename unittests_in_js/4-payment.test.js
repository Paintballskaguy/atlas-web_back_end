const sinon = require('sinon')
const chai = require('chai')
const expect = chai.expect
const Utils = require('./utils')
const sendPaymentRequestToApi = require('./4-payment')

describe('sendPaymentRequestToApi', () => {
  let calculateNumberStub
  let consoleSpy

  beforeEach(() => {
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10)
    consoleSpy = sinon.spy(console, 'log')
  })

  afterEach(() => {
    calculateNumberStub.restore()
    consoleSpy.restore()
  })

  it('should call Utils.calculateNumber with SUM, 100, and 20', () => {
    sendPaymentRequestToApi(100, 20)

    expect(calculateNumberStub.calledOnce).to.be.true
    expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true
  })

  it('should log "The total is: 10" to the console', () => {
    sendPaymentRequestToApi(100, 20)

    expect(consoleSpy.calledOnce).to.be.true
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true
  })
})
