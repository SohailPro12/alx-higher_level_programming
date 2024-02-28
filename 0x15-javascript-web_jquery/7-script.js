/*
fetches the character name from this URL: 
https://swapi-api.alx-tools.com/api/people/5/?format=json
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
  <script>
    $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(response) {
       $('character').text(response.name);
    }
    });
  </script>;
