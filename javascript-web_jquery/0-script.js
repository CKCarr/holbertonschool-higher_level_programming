#!/usr/bin/node
/* 0. No JQuery 
Write a JavaScript script that updates the text color of the <header> element to red (#FF0000):
    You must use document.querySelector to select the HTML tag
    You can’t use the JQuery API
 */
function updateHeaderTextColor() {
    const headerElement = document.querySelector('header');
    headerElement.style.color = '#FF0000';
}
updateHeaderTextColor();
