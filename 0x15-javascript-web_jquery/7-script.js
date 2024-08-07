/** fetches the character name from this
 * URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
*/

$(document).ready(function () {
  $.ajax(
    {
      url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
      method: 'GET',
      success: (body, statusCode, xhr) => {
        $('#character').text(body.name);
      },
      error: (xml, error, exc) => {
        console.log('Error in ajax request');
      }
    }
  );
});
