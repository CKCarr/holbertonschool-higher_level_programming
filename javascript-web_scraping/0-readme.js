#!/usr/bin/node
/* Write a script that reads and prints the content of a file.

    The first argument is the file path
    The content of the file must be read in utf-8
    If an error occurred during the reading, print the error object
 */
// import 'fs' module : fs = "File System"
const fs = require('fs');
// command line args when you run node.js script index[2] is file path
// usage: (./ =)node[0] thisfilescript.js[1] file2read[2]
// from task example: ./[0]0-readme.js[1] cisfun[2]
// from task example: ./[0]0-readme.js[1] doesntexist[2]
const filePath = process.argv[2];
/* The 'fs.readFile()' method reads the content of the file asynchronously.
It takes three arguments:
1. The file path to read.
2. The encoding to use while reading the file. 
    In this case, 'utf-8' is used to read the file as a text file.
3. A callback function that will be called
    when the reading is complete or an error occurs. */
fs.readFile(filePath, 'utf-8', (err,data) => {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
});
