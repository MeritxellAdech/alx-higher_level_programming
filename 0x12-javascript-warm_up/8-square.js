#!/usr/bin/node
const { argv } = require('process');

function square (size) {
  if (!Number(size)) {
    console.log('Missing size');
    return;
  }

  let index = 0;
  let row = '';
  let i = 0;
  // let flagToPrint = false;
  const times = Number(size);

  while (index < times) {
    while (i < times) {
      row += 'X';
      i++;
    }
    console.log(row);
    index++;
  }

  // while (index < times) {
  //   if (!flagToPrint) {
  //     row += 'X';
  //   } else {
  //     console.log(row);
  //   }

  //   index++;

  //   if (index === times && !flagToPrint) {
  //     flagToPrint = true;
  //     index = 0;
  //   }
  // }
}

square(argv[2]);
