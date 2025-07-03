const chai = require('chai')
const expect = chai.expect
const calculateNumber = require('./2-calcul_chai')

describe('calculateNumber', () => {
  describe('SUM operation', () => {
    it('should return the sum of rounded numbers', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6)
      expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6)
      expect(calculateNumber('SUM', 1.2, 3.3)).to.equal(4)
    })
  })

  describe('SUBTRACT operation', () => {
    it('should return the difference of rounded numbers', () => {
      expect(calculateNumber('SUBTRACT', 5.5, 3.3)).to.equal(3)
      expect(calculateNumber('SUBTRACT', 10.9, 2.1)).to.equal(9)
      expect(calculateNumber('SUBTRACT', 7.6, 2.4)).to.equal(6)
    })
  })

  describe('DIVIDE operation', () => {
    it('should return the quotient of rounded numbers', () => {
      expect(calculateNumber('DIVIDE', 10, 2)).to.equal(5)
      expect(calculateNumber('DIVIDE', 9.5, 2.1)).to.equal(5)
      expect(calculateNumber('DIVIDE', 12, 3.7)).to.equal(3)
    })

    it('should return "Error" when dividing by zero', () => {
      expect(calculateNumber('DIVIDE', 10, 0.4)).to.equal('Error')
      expect(calculateNumber('DIVIDE', 8.7, 0)).to.equal('Error')
      expect(calculateNumber('DIVIDE', 5.2, -0.3)).to.equal('Error')
    })
  })

  describe('Invalid operation type', () => {
    it('should throw an error for invalid operation type', () => {
      expect(() => calculateNumber('MULTIPLY', 5, 3)).to.throw(
        Error,
        'Invalid operation type'
      )
    })
  })
})
