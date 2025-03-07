export default class Airport {
  constructor(name, code) {
    // Verify then set name and code //
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = name;

    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = code;
  }

  //  getter for name and code //
  get name() {
    return this._name;
  }

  get code() {
    return this._code;
  }

  // new toString method for this only //
  toString() {
    return `[object ${this._code}]`;
  }
}
