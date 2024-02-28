#!/usr/bin/node
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>List Manipulation</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script>
    $(document).ready(function() {
      $("#add_item").click(function() {
        $("ul.my_list").append("<li>Item</li>");
      });

      $("#remove_item").click(function() {
        $("ul.my_list li:last").remove();
      });

      $("#clear_list").click(function() {
        $("ul.my_list").empty();
      });
    });
  </script>
</head>
<body>
  <div id="add_item">Add Item</div>
  <div id="remove_item">Remove Item</div>
  <div id="clear_list">Clear List</div>
  <ul class="my_list"></ul>
</body>
</html>

