#!/usr/bin/node
/* Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:
    You must use the class notation for defining your class and extends
    The constructor must take 1 argument: size
    The constructor of Rectangle must be called (by using super())
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // Class Square is an inheritance of a Rectangle object
  constructor (size) {
    // Call the constructor of the Rectangle class using super()
    // height and width are both the size . equal to create square
    super(size, size);
  }
}

module.exports = Square;
