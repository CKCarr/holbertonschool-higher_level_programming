#!/usr/bin/node
/* Write a script that computes the number of tasks completed by user id.

    The first argument is the API URL:
    https://jsonplaceholder.typicode.com/todos
    Only print users with completed task
    You must use the module request
*/
// import modules needed
const request = require('request');

// 1st command line arguments is api url
const apiUrl = process.argv[2];

// make an HTTP [GET] request with callback function
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else if (response.statusCode !== 200) {
    console.error('Error status code:', response.statusCode);
  } else {
    // parse the response body as JSON
    const parsedBody = JSON.parse(body);
    // initialize an object to store completed tasks count by userID
    const completedTasks = {};
    // Loop throught the array to count completed tasks
    for (let i = 0; i < parsedBody.length; i++) {
      // extract userId from JSON parse array
      const userID = parsedBody[i].userId;
      // if body contains completed
      if (parsedBody[i].completed) {
        // store and increment all completed tasks for userId
        if (completedTasks[userID]) {
          completedTasks[userID]++;
        } else {
          completedTasks[userID] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
