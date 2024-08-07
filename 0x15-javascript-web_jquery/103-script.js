/* script that fetches from
 *  https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value
 * of hello from that fetch in the HTML tag DIV#hello.
 * 
 * he translation must be fetched when the user clicks on 
 * INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
*/

$(document).ready(function () {
  const getData = function () {
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
  };

  $('#language_code').on('keypress', function (key) {
    if (key.which === 13) {
      getData();
    }
  });
  $('#btn_translate').on('click', function () {
    getData();
  });
});
