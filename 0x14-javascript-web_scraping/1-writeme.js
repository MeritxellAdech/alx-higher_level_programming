#!/usr/bin/node
const { writeFile } = require('node:fs');
const { argv } = require('process');

//  writing into the file
writeFile(argv[2], argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
