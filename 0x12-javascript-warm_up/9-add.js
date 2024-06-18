#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  if (!Number(a) || !Number(b)) {
    console.log('NaN');
    return;
  }
  const result = Number(a) + Number(b);
  console.log(result);
}

add(argv[2], argv[3]);
