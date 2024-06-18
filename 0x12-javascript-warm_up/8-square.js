#!/usr/bin/node
const { argv } = require('process');

function square (size) {
  if (isNaN(parseInt(size))) {
    console.log('Missing size');
    return;
  }

  let i = 0;
  let j = 0;
  let row = '';
  const times = parseInt(size);
  while (i < times) {
    while (j < times) {
      row += 'x';
      j++;
    }
    console.log(row);
    i++;
  }
}

square(argv[2]);
