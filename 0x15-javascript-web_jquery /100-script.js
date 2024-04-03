<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Header Color</title>
    <script>
        // Select the <header> element and update its text color to red
        document.addEventListener('DOMContentLoaded', function() {
            var header = document.querySelector('header');
            if (header) {
                header.style.color = '#FF0000';
            }
        });
    </script>
</head>
<body>
    <header>
        This is the header
    </header>
    <!-- Other HTML content -->
</body>
</html>
      
