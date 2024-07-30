#!/usr/bin/node
// write content from file

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {   // eslint-disable-line
  console.log(`code: ${response.statusCode}`);
});
