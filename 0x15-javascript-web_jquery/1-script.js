/*
updates the text color of the <header> element to red (#FF0000)
using JQuery API
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
$(document).ready(function () {
  const element = $('header');
  element.css('color', 'red');
});
