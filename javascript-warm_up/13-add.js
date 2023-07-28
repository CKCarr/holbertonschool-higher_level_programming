#!/usr/bin/node
/* 13. Add file
Write a function that returns the addition of 2 integers.
    The function must be visible from outside
    The name of the function must be add
    You are not allowed to use var
 */

// function that adds two ints
function add (a, b) {
  return a + b;
}

// Export add() function to make it visible from outside
module.exports = add;
