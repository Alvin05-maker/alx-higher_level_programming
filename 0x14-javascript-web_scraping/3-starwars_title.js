#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const episodeNum = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episodeNum;

request(url, function (err, response, body) {   // eslint-disable-line
  console.log(JSON.parse(body).title);
});
