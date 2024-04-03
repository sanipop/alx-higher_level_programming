<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Translation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            $('#btn_translate').click(function() {
                var languageCode = $('#language_code').val();
                $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(response) {
                    $('#hello').text(response.hello);
                });
            });
        });
    </script>
</head>
<body>
    <input type="text" id="language_code" placeholder="Enter language code (e.g., es, fr, en)">
    <input type="button" id="btn_translate" value="Translate">
    <div id="hello"></div>
</body>
</html>
