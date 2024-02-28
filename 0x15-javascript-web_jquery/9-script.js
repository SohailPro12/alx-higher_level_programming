/*
fetches all titles from this URL: 
https://hellosalut.stefanbohacek.dev/?lang=fr
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
  <script>
    $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function(response) {
        $('#hello').text(data.hello)
        }
    });
  </script>;
