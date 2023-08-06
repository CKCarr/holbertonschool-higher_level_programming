#!/usr/bin/node
/* 8. Star Wars movies 
Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

    All movie titles must be list in the HTML tag UL#list_movies
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
 */
$(function () {
    $.ajax({
        type: 'GET',
        url: 'https://swapi-api.hbtn.io/api/films/?format=json',
        success: function (data) {
            // extract movie titles from JSON
            let movies = data.results;
            // move through each movie and create list for titles
            $('#list_movies').empty();
            $.each(movies, function (index, movie) {
                let movieTitle = movie.title;
                $('#list_movies').append('<li>' + movieTitle + '</li>');
            });
        },
        error: function (error) {
            console.log('Error fetching movie data:', error)
        }
    });
});
