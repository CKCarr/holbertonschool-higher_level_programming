#!/usr/bin/node
/* Write a script that display the status code of a GET request.

    The first argument is the URL to request (GET)
    The status code must be printed like this: code: <status code>
    You must use the module request
 */
// import module request module to make HTTP requests
const request = require('request');
// array of cmd line args: arg[2] is url, to request [GET]
const url = process.argv[2];

// two args, url request && callback function for error and status code
request(url, (error, response) => {
  if (error) {
    console.error(error.message);
  } else {
    // 200: for success || 404: for not found
    console.log(`code: ${response.statusCode}`);
  }
});
