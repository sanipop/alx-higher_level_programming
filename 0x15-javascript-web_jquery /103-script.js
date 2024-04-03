//task 103
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Translation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            // Function to fetch translation
            function fetchTranslation() {
                var languageCode = $('#language_code').val();
                $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(response) {
                    $('#hello').text(response.hello);
                });
            }

            // Fetch translation when the user clicks on btn_translate
            $('#btn_translate').click(fetchTranslation);

            // Fetch translation when the user presses ENTER in language_code input
            $('#language_code').keypress(function(event) {
                if (event.keyCode === 13) { // Enter key
                    fetchTranslation();
                }
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
