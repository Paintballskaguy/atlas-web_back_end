import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    // Verify amount and currency //
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = amount;

    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be an instance of Currency');
    }
    this._currency = currency;
  }

  // getter and setter for amount and currency //
  get amount() {
    return this._amount;
  }

  set amount(newAmount) {
    if (typeof newAmount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this._amount = newAmount;
  }

  get currency() {
    return this._currency;
  }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) {
      throw new TypeError('Currency must be an instance of Currency');
    }
    this._currency = newCurrency;
  }

  // Display the full price, hopefully //

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}
