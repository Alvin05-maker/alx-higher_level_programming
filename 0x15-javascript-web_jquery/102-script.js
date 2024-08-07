/* script that fetches from
 *  https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value
 * of hello from that fetch in the HTML tag DIV#hello.
*/

$(document).ready(function () {
  $('#btn_translate').click(function () {
    $.ajax(
      {
        url: 'https://hellosalut.stefanbohacek.dev/',
        type: 'GET',
        data: {
          lang: $('#language_code').val()
        },

        success: (data, statusCode, xhr) => {
          console.log($('#language_code').val());
          $('#hello').text(data.hello);
        },

        error: (xml, error, exc) => {
          console.log('Error in ajax request');
        }
      }
    );
  });
});
