export default class Building {
  constructor(sqft) {
    // Verify sqft //
    if (typeof sqft !== 'number') {
      throw new TypeError('sqft must be a number');
    }
    this._sqft = sqft;

    if (this.constructor !== Building && typeof this.evacuationWarningMessage !== 'function') {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // Getter sqft
  get sqft() {
    return this._sqft;
  }
}
