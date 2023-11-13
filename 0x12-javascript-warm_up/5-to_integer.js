#!/usr/bin/node
const firstArg = process.argv[2];
let concatString = '';

if (typeof firstArgv == 'number') 
{
	concatString = 'My number:' + " " + firstArg;
	console.log(concatString);
}
else {
	console.log('Not a number');
}
