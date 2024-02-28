#!/usr/bin/node
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Update Header Color</title>
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      var header = document.querySelector("header");
      header.style.color = "#FF0000"; // sets the text color to red
    });
  </script>
</head>
<body>
  <header>This is the header</header>
</body>
</html>

