/*
Changing the text of a header
using JQuery API when clicking on a div
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
  <script>
    var element = $('header');
    var div = $('update_header');
    div.on('click', function() {
        element.text("New Header!!!")
    });
  </script>;
