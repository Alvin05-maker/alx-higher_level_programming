#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
}
const array = process.argv.slice(2).map(Number);
const secondNum = array.sort(function (a, b) { b - a; })[1];
console.log(secondNum);
