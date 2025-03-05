export default class Currency {
  constructor(code, name) {
    // tester to make sure name, length and students meet requirements//

    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = code;

    if (typeof name !== 'string') {
      throw new TypeError('name must be a number');
    }
    this._name = name;
  }

  // getting and setting together because this is easier. //

  get code() {
    return this._code;
  }

  set code(newCode) {
    if (typeof newCode !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = newCode;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = newName;
  }
}
