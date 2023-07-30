#!/usr/bin/node
/* 6. Square #1
Write a class Square that defines a square and inherits from Square of 5-square.js:

    You must use the class notation for defining your class and extends
    Create an instance method called charPrint(c) that prints the rectangle using the character c
        If c is undefined, use the character X
 */

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  constructor (size) {
    super(size, size);
  }

  // instance method
  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    const row = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
