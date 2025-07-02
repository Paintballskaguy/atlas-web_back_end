const assert = require('assert')
const calculateNumber = require('./1-calcul')

describe('calculateNumber', () => {
  describe('SUM operation', () => {
    it('should return 6 when inputs are 1.4 and 4.5', () => {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6)
    })

    it('should return 0 when inputs are -0.4 and 0.4', () => {
      assert.strictEqual(calculateNumber('SUM', -0.4, 0.4), 0)
    })

    it('should return -2 when inputs are -1.4 and -0.5', () => {
      assert.strictEqual(calculateNumber('SUM', -1.4, -0.5), -1)
    })
  })

  describe('SUBTRACT operation', () => {
    it('should return -4 when inputs are 1.4 and 4.5', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4)
    })

    it('should return 0 when inputs are 0.5 and 0.5', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 0.5, 0.5), 0)
    })

    it('should return 1 when inputs are 1.5 and 0.5', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.5, 0.5), 1)
    })
  })

  describe('DIVIDE operation', () => {
    it('should return 0.2 when inputs are 1.4 and 4.5', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2)
    })

    it('should return "Error" when dividing by 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error')
    })

    it('should return "Error" when rounded divisor is 0', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error')
    })

    it('should return 2 when inputs are 5.5 and 2.7', () => {
      assert.strictEqual(calculateNumber('DIVIDE', 5.5, 2.7), 2)
    })
  })

  describe('Edge cases', () => {
    it('should throw error for invalid type', () => {
      assert.throws(() => calculateNumber('MULTIPLY', 1, 2), Error)
    })

    it('should handle large numbers', () => {
      assert.strictEqual(calculateNumber('SUM', 1e20, 1e20), 2e20)
    })

    it('should handle very small numbers', () => {
      assert.strictEqual(calculateNumber('SUBTRACT', 1e-20, 1e-20), 0)
    })
  })
})
