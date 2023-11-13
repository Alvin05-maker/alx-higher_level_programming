#!/usr/bin/node
let concatString = '';
if (process.argv.length <= 2) {
  process.argv[2] = 'undefined';
  process.argv[3] = 'undefined';
} else {
  concatString += process.argv[2] + ' ' + 'is' + ' ' + process.argv[3];
}
console.log(concatString);
