export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Getter for brand, motor and color //
  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  // clone the car here for other models //
  cloneCar() {
    const Constructor = Object.getPrototypeOf(this).constructor;
    return new Constructor();
  }
}
