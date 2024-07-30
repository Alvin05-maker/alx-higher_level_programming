#!/usr/bin/node
// prints the number of movies where the character “Wedge Antilles” is present.
// Wedge Anitilles is character with id=18

const request = require('request');
const id = '/18/';
const url = process.argv[2];

request(url, function (err, response, body) {   // eslint-disable-line
  const allFilms = JSON.parse(body);
  let wedgeAntillesFilmCount = 0;

  allFilms.results.forEach(film => {
    film.characters.forEach(characterUrl => {
      if (characterUrl.includes(id)) {
        wedgeAntillesFilmCount++;
      }
    });
  });

  console.log(wedgeAntillesFilmCount);
});
