#!/usr/bin/node
/* 2. Rectangle #2
Write a class Rectangle that defines a rectangle:
    You must use the class notation for defining your class
    The constructor must take 2 arguments w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object
 */

class Rectangle {
  constructor (w, h) {
    const isNonPositiveInt = (w <= 0 || h <= 0);
    const isNotInt = (!Number.isInteger(w) || !Number.isInteger(h));

    if (isNonPositiveInt || isNotInt) {
      // If w or h = 0 or not positive ints, create an empty object
      return {};
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
