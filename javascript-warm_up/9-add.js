#!/usr/bin/node
/* 9. Add
Write a script that prints the addition of 2 integers
    The first argument is the first integer
    The second argument is the second integer
    You have to define a function with this prototype: function add(a, b)
    You must use console.log(...) to print all output
    You are not allowed to use var
 */

// create variables for command line args
const int1 = process.argv[2];
const int2 = process.argv[3];

// create function to add ints
function add (int1, int2) {
  return (int1 + int2);
}
// parse and convert command line args to ints
const parInt1 = parseInt(int1);
const parInt2 = parseInt(int2);

// check if one or the other are NaN for output: NaN :: not else{"log"}
if (!isNaN(parInt1) || !isNaN(parInt2)) {
  // create variable for result and call function on parsed cli args
  const result = add(parInt1, parInt2);
  console.log(result);
} else {
  // if commline args are NaN
  console.log('Invalid arguments. Please provide two integers');
}
