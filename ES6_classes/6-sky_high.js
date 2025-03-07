import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);

    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    this._floors = floors;
  }

  // getter for the floors //
  get floors() {
    return this._floors;
  }

  // overriding the warning message from Building //
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
