#!/usr/bin/node
// read content from file

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', function (err, content) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(content);
});
