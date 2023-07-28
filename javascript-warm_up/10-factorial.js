#!/usr/bin/node
/* 10. Factorial
Write a script that computes and prints a factorial
    The first argument is integer (argument can be cast as integer) used for computing the factorial
    Factorial of NaN is 1
    You must do it recursively
    You must use a function
    You must use console.log(...) to print all output
    You are not allowed to use var
*/

// create function to calculate factorial through recursion
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 1;
  }
  // This recursive call will continue until n becomes 0
  return (n * factorial(n - 1));
}
// create variable for command line arg
const numberArg = parseInt(process.argv[2]);
// create result variable for factorial calculation of cli arg
const result = factorial(numberArg);
// output:  arg = n,  factorial of n
console.log(result);
