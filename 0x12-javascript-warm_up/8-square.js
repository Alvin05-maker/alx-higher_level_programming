#!/usr/bin/node
const firstArg = process.argv[2];
if (firstArg === undefined || isNaN(firstArg)) {
  console.log('Missing size');
} else {
  const x = parseInt(firstArg);
  let index = 0;
  while (index < x) {
    console.log('X'.repeat(x));
    index++;
  }
}
