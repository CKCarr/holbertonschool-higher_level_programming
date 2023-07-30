#!/usr/bin/node
/* 3. Rectangle #3
Write a class Rectangle that defines a rectangle
    You must use the class notation for defining your class
    The constructor must take 2 arguments: w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
    If w or h is equal to 0 or not a positive integer, create an empty object
    Create an instance method called print() that prints the rectangle using the character X
*/

class Rectangle {
  /* Rectangle class with 2 args w & h */
  constructor (w, h) {
    const isNonPositiveInt = (w <= 0 || h <= 0);
    const isNotInt = (!Number.isInteger(w) || !Number.isInteger(h));

    if (isNonPositiveInt || isNotInt) {
      // If w or h = 0 or not positive ints, create an empty object
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (!this.width || !this.height) {
      // empty object print empty line
      console.log();
    } else {
      const row = 'X'.repeat(this.width);
      for (let col = 0; col < this.height; col++) {
        console.log(row);
      }
    }
  }

  rotate () {
    // exchange the width and the height
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Double the width and height
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
