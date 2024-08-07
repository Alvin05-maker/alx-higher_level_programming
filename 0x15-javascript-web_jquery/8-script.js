/** fetches and lists the title for all movies by using this
 * URL: https://swapi-api.alx-tools.com/api/films/?format=json
*/

$(document).ready(function () {
  $.ajax(
    {
      url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
      type: 'GET',

      success: (body, statusCode, xhr) => {
        $.each(body.results, function (index, item) {
          $('#list_movies').append('<li>' + item.title + '</li>');
        });
      },

      error: (xml, error, exc) => {
        console.log('Error in ajax request');
      }
    }
  );
});
