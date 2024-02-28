/*
fetches the character name from this URL: 
https://swapi-api.alx-tools.com/api/people/5/?format=json
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
    <script>
    $('#btn_translate').click(function () {
        const languageCode = $('#language_code').val();
        const urlApi = 'https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}';
        $.getJSON(urlApi, function (data) {
        $('#hello').text(data.hello);
        });
    });
    $('#language_code').keypress(function (event) {
        if (event.keyCode === 13) {
        $('#btn_translate').click();
        }
    });
    </script>;
