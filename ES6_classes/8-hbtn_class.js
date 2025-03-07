export default class HolbertonClass {
  constructor(size, location) {
    // Verify then set the size and location //

    if (typeof size !== 'number') {
      throw new TypeError('Size must be a number');
    }
    this._size = size;

    if (typeof location !== 'string') {
      throw new TypeError('Location must be a string');
    }
    this._location = location;
  }

  //  getter stuff //
  get size() {
    return this._size;
  }

  get location() {
    return this._location;
  }

  // returning the size of as number //
  valueOf() {
    return this._size;
  }

  // override toSttring for this method only //
  toString() {
    return this._location;
  }
}
