#!/usr/bin/node
/* 8. Square
Write a script that prints a square
    The first argument is the size of the square
    If the first argument can’t be converted to an integer, print “Missing size”
    You must use the character X to print the square
    You must use console.log(...) to print all output
    You are not allowed to use var
    You must use a loop (while, for, etc.)
 */

// parse string of argv & convert to int or return NAN
const argSize = parseInt(process.argv[2]);

// if arg can be converted = True
if (!isNaN(argSize)) {
  // outer loop reps rows of square
  for (let row1 = 0; row1 < argSize; row1++) {
    // empty string stores X char for each row
    let row = '';
    // reps columns for square
    for (let col1 = 0; col1 < argSize; col1++) {
      // appends an 'X' char to row
      row += 'X';
    }
    console.log(row);
  }
} else {
  // if argSize is NaN
  console.log('Missing size');
}
