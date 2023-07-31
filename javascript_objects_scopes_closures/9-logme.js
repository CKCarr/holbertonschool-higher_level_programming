#!/usr/bin/node
/* 9. Log me
Write a function that prints the number of arguments already printed and the new argument value. (see example below)
    Prototype: exports.logMe = function (item)
    Output format: <number arguments already printed>: <current argument value>
 */
// count to keep track of arguments already printed
let count = 0;
exports.logMe = function (item) {
  console.log(count + ':' + item);
  count++;
};
