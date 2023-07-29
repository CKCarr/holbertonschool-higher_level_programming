#!/usr/bin/node
/* 13. Add file
Write a function that returns the addition of 2 integers.
    The function must be visible from outside
    The name of the function must be add
    You are not allowed to use var
 */

// Function that returns the addition of 2 integers
function add(a, b) {
  return a + b;
}

// Export the 'add' function to make it visible from outsid
exports.add = add;
