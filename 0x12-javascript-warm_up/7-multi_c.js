#!/usr/bin/node
const firstArg = process.argv[2];
if (firstArg === undefined || isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(firstArg);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
