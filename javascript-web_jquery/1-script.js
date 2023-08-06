#!/usr/bin/node
/* 1. With JQuery 
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):
    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
 */
$(document).ready(function () {
    // grab header and update css color to red
    $('header').css('color', '#FF0000');
});
