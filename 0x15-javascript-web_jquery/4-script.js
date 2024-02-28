// Toggle the class of the <header> element when the user clicks on the
// `DIV#toggle_header` tag. classes are red and green

$(document).ready(() => {
  $('DIV#toggle_header').on('click', () => {
    $('header').toggleClass('red green');
  });
});
