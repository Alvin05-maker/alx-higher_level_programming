#!/usr/bin/node

let i = 0;
const arg1 = process.argv[2];
const occurNum = parseInt(arg1);

if (isNaN(occurNum)) {
  console.log('Missing number of occurrences');
} else {
  while (i < occurNum) {
    console.log('C is fun');
    i++;
  }
}
