/**
 * update the header of the html when the update_header is clicked
 */

$(document).ready(function () {
  $('#update_header').on('click', function () {
    $('header').text('New Header!!!');
  });
});
