/*
updates the text color of the <header> by toggling between red and green
using JQuery API when clicking on a div
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
  <script>
    const element = $('header');
    var div = $('#red_header');
    div.on('click', function() {
        element.toggleClass('red green')
    });
  </script>;
