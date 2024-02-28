<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Translate Hello</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script>
    $(document).ready(function() {
      $("#language_code").on("keypress", function(e) {
        if (e.which === 13) {
          fetchTranslation();
        }
      });

      $("#btn_translate").click(function() {
        fetchTranslation();
      });

      function fetchTranslation() {
        var languageCode = $("#language_code").val();
        var apiURL = "https://www.fourtonfish.com/hellosalut/hello/";

        $.getJSON(apiURL + languageCode, function(data) {
          $("#hello").text(data.hello);
        }).fail(function() {
          $("#hello").text("Translation not found");
        });
      }
    });
  </script>
</head>
<body>
  <input type="text" id="language_code" placeholder="Enter language code (ex: es, fr, en)">
  <input type="button" id="btn_translate" value="Translate">
  <div id="hello"></div>
</body>
</html>

