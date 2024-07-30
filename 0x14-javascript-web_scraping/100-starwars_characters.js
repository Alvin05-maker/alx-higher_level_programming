#!/usr/bin/node
// prints all characters of a Star Wars movie: using the movie id

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, function (err, response, body) {   // eslint-disable-line
  if (err) {
    return;
  }
  const characters = JSON.parse(body).characters;

  characters.forEach(character => {
    request(character, function (err, response, body) {
      if (err) {
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
