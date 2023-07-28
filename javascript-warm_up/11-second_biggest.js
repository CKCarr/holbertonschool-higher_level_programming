#!/usr/bin/node
/* 11. Second biggest!
Write a script that searches the second biggest integer in the list of arguments.
    You can assume all arguments can be converted to integer
    If no argument passed, print 0
    If the number of arguments is 1, print 0
    You must use console.log(...) to print all output
    You are not allowed to use var
 */

// function to map and parse args to ints, remove dups, and sort 2 args
// with the array given as output: array[1] will be the second biggest
function findSecondBiggest (args) {
  const ints = args.map(arg => parseInt(arg));
  const uniqInts = Array.from(new Set(ints));
  const sortedInts = uniqInts.sort((a, b) => b - a);

  return sortedInts[1] || 0;
}

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const seconbBiggest = findSecondBiggest(args);
  console.log(seconbBiggest);
}
