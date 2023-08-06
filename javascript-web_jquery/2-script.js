#!/usr/bin/node
/* 2. Click and turn red
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:

    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
 */
$(function () {
    $('#red_header').on('click', function () {
        $('header').css('color', '#FF0000');
    });
});
