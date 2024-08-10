/**
 * This file changes the content of the header to 'New Header!!!'
 * when the user clicks div#update_header
 */

$('#update_header').click(function () {
  $('header').text('New Header!!!');
});
