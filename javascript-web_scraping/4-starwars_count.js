#!/usr/bin/node
/* Write a script that prints the number of movies where the character “Wedge Antilles” is present.
    The first argument is the API URL of the Star wars API:
    https://swapi-api.hbtn.io/api/films/
    Wedge Antilles is character ID 18 -
    your script must use this ID for filtering the result of the API
    You must use the module request
*/
// required modules
const request = require('request');
// first argument is the API URL
const apiUrl = process.argv[2];

// function to count movies with "Wedge Antilles" char ID 18 present
request(apiUrl, (error, response, body) => {
  if (error) {
    return console.log(error);
  }
  // parse body as JSON and get results array
  const parsedBody = JSON.parse(body).results;
  // initialize count to keep track of occurrences
  let count = 0;
  // loop through the results array
  for (let i = 0; i < parsedBody.length; i++) {
    // find characters array in each 'results' element
    const characters = parsedBody[i].characters;
    // check if character array has ID 18
    const personID18 = characters.find((person) => person.includes('18'));
    // if a character with ID 18 is found increment the count
    if (personID18) {
      count++;
    }
  }
  // Print the final count of occurrences of characters with ID 18
  console.log(count);
});
