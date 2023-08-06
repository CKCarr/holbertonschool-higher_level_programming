#!/usr/bin/node
/* 9. Say Hello! 
Write a JavaScript script that fetches from https://stefanbohacek.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

    The translation of “hello” must be displayed in the HTML tag DIV#hello
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
    Your script must work when it is imported from the <head> tag
 */
function displayHello(data) {
    $('#hello').text(data.hello);
}

$(document).ready(function () {
    $.ajax({
        url: 'https://cors-anywhere.herokuapp.com/https://stefanbohacek.com/hellosalut/?lang=fr',
        dataType: 'jsonp',
        jsonpCallback: 'displayHello',
        success: function (data) {
            // This function will be executed when the JSONP response is received.
            // The JSONP response should contain the "hello" data.
        },
        error: function () {
            $('#hello').text('Error fetching data');
        }
    });
});

