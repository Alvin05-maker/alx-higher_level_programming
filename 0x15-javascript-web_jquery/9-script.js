/* script that fetches from
 *  https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value
 * of hello from that fetch in the HTML tag DIV#hello.
*/

$(document).ready(function () {
  $.ajax(
    {
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      type: 'GET',

      success: (data, statusCode, xhr) => {
        $('#hello').text(data.hello);
      },

      error: (xml, error, exc) => {
        console.log('Error in ajax request');
      }
    }
  );
});
