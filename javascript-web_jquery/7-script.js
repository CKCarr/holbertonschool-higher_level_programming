#!/usr/bin/node
/* 7. Star wars character 
Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

    The name must be displayed in the HTML tag DIV#character
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
 */
$(function () {
    // Fetch character data from the URL using AJAX
    $.ajax({
        url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
        type: 'GET',
        success: function (data) {
            // Extract the character name from the JSON response
            let characterName = data.name;

            // Update HTML content of 'DIV#character' with the character name
            $('#character').text(characterName);
        }
    });
});

