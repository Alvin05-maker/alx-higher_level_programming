#!/usr/bin/node
function add (a, b) {
  if ((a || b) === undefined || isNaN(a || b)) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
