#!/usr/bin/node
/* 1. Rectangle #1
Write a class Rectangle that defines a rectangle:
    You must use the class notation for defining your class
    The constructor must take 2 arguments w and h
    Initialize the instance attribute width with the value of w
    Initialize the instance attribute height with the value of h
 */

class Rectangle {
  /* Rectangle class with 2 args w & h */
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
