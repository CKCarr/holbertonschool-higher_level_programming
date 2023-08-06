#!/usr/bin/node
/* 3. Add `.red` class 
Write a JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header

    You can’t use document.querySelector to select the HTML tag
    You must use the JQuery API
 */
function DocumentReady() {
    $('#red_header').click(function () {
        $('header').addClass('red');
    });
}
$(document).ready(DocumentReady);
