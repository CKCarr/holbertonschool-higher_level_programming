#!/usr/bin/node
/*
Write a script that prints x times “C is fun”
    Where x is the first argument of the script
    If the first argument can’t be converted to an integer, print “Missing number of occurrences”
    You must use console.log(...) to print all output
    You are not allowed to use var
    You can use only two console.log
    You must use a loop (while, for, etc.)
 */

// parse string of argv & convert to int or return NAN
const argX = parseInt(process.argv[2]);

// if arg can be converted = True
if (!isNaN(argX)) {
  // loop to iterate until i = x & print string*i to reach x
  for (let i = 0; i < argX; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
