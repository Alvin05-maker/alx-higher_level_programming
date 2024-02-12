#!/usr/bin/node

const arg1 = process.argv[2];
const size = parseInt(arg1);
const x = 'X';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let y = 0; y < size; y++) {
    console.log(x.repeat(size));
  }
}
