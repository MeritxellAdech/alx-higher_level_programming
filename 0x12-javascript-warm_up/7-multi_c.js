#!/usr/bin/node
const { argv } = require('process');

function printing (value) {
  if (isNaN(parseInt(value))) {
    console.log('Missing number of occurrences');
    return;
  }
  let i = 0;
  while (i < value) {
    console.log('C is fun');
    i++;
  }
}

printing(argv[2]);
