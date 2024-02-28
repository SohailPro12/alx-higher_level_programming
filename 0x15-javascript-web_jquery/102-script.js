/*
fetches and prints how to say “Hello” depending on the languge
*/
<script src='https://code.jquery.com/jquery-3.2.1.min.js' />;
    <script>
    $(document).ready(function () {
        $('#btn_translate').click(function () {
        const languageCode = $('#language_code').val();
        const urlApi = 'https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}';
    
        $.get(urlApi, function (data) {
            $('#hello').text(data.hello);
        });
        });
    });
    </script>
