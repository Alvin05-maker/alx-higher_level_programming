#!/usr/bin/node

const arg1 = process.argv[2];
const parsedNumber = parseInt(arg1);

if (isNaN(parsedNumber)) {
  console.log('Not a number');
} else {
  console.log('My number:' + ' ' + parsedNumber);
}
