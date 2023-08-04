#!/usr/bin/node
/* Write a script that writes a string to a file.
    The first argument is the file path
    The second argument is the string to write
    The content of the file must be written in utf-8
    If an error occurred during while writing, print the error object
*/
// imports File System module
const fs = require('fs');

// cmd line args for file path
const filePath = process.argv[2];
// cmd line arg for string to be written to file
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
