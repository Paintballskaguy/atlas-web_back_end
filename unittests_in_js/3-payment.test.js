const sinon = require('sinon')
const chai = require('chai')
const expect = chai.expect
const Utils = require('./utils')
const sendPaymentRequestToApi = require('./3-payment')

describe('sendPaymentRequestToApi', () => {
  it('should call Utils.calculateNumber with SUM type and correct arguments', () => {
    // create a spy on Utils.calculateNumber
    const calculateNumberSpy = sinon.spy(Utils, 'calculateNumber')

    // call the function we're testing
    sendPaymentRequestToApi(100, 20)

    // verify the spy was called correctly
    expect(calculateNumberSpy.calledOnce).to.be.true
    expect(calculateNumberSpy.calledWith('SUM', 100, 20)).to.be.true

    // restore the spy
    calculateNumberSpy.restore()
  })

  it('should log the correct total to the console', () => {
    const calculateNumberStub = sinon
      .stub(Utils, 'calculateNumber')
      .returns(120)

    // spy on console.log
    const consoleSpy = sinon.spy(console, 'log')

    sendPaymentRequestToApi(100, 20)

    // verify console.log was called with the right message
    expect(consoleSpy.calledWith('The total is: 120')).to.be.true

    // restore all spies/stubs
    calculateNumberStub.restore()
    consoleSpy.restore()
  })
})
