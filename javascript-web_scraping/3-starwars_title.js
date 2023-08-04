#!/usr/bin/node
/* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

    The first argument is the movie ID
    You must use the Star wars API with the endpoint
    https://swapi-api.hbtn.io/api/films/:id
    You must use the module request
*/
// import request to handle http GET
const request = require('request');
// First arg is movie ID to use parse films and return title of movie
const movieID = process.argv[2];
// cmd line argv[1]: Star wars API
const urlEndpoint = `https://swapi-api.hbtn.io/api/films/${movieID}`;

request(urlEndpoint, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
  } else if (response.statusCode !== 200) {
    console.error('Error:', body);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
