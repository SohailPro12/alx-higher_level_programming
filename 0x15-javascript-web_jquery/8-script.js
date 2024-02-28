/*
fetches all titles from this URL: 
https://swapi-api.alx-tools.com/api/films/?format=json
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
  <script>
    $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(response) {
        $.each(response.results, function (index, movie) {
            $('<li>').text(movie.title).appendTo('#list_movies');
          })
        }
    });
  </script>;
