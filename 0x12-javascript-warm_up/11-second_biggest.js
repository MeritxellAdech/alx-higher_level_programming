#!/usr/bin/node
const { argv } = require('process');

function bigsecond (args) {
  if (args.length === 2 || args.length === 3) {
    return (0);
  }
  let big = Number(args[2]);
  let sec = 0;
  let i = 2;
  while (i < (args.length)) {
    if (Number(args[i]) > big) {
      sec = big;
      big = Number(args[i]);
    }
    // Set the second biggest number
    if (Number(args[i]) > sec && Number(args[i]) < big) {
      sec = Number(args[i]);
    }
    i++;
  }
  return (sec);
}

console.log(bigsecond(argv));
