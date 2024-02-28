/*
Adding an item to a list
using JQuery API when clicking on a div
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
  <script>
    var div = $('add_item');
    div.on('click', function() {
        $('<li>Item</li>').appendTo('.my_list')
    });
  </script>;
