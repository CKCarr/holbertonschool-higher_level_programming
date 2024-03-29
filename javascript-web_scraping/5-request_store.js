#!/usr/bin/node
/* Write a script that gets the contents of a webpage and stores it in a file.

    The first argument is the URL to request
    The second argument the file path to store the body response
    The file must be UTF-8 encoded
    You must use the module request
*/
// import modules
const fs = require('fs');
const request = require('request');

// command line arguments
const apiUrl = process.argv[2];
const filePath = process.argv[3];

// request given url with a callback function for error or success of url
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else {
    // use fs to write to file w/ callback function upon error or success
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err.message);
      }
    });
  }
});
