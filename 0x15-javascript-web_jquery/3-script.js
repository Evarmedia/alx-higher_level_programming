// Adds the class `red` to the <header> tag when user clicks `DIV#red_header`
// using jQuery api

$(document).ready(() => {
  $('DIV#red_header').on('click', () => {
    $('header').addClass('red');
  });
});

