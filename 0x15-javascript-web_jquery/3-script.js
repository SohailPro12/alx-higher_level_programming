/*
updates the text color of the <header> element to red (#FF0000)
using JQuery API when clicking on a div
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
  <script>
    const element = $('header');
    var div = $('#red_header');
    div.on('click', function() {
        element.addClass('red')
    });
  </script>;
