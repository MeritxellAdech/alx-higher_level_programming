#!/usr/bin/node
const { argv } = require('process');
const { readFile } = require('node:fs');

// Accessing the file
const file = argv[2];
// printing the content of the file
readFile(file, 'utf8', (err, data) => {
  // The file does not exist or it is empty
  if (err) {
    console.error(err);
    return;
  }
  // print the data within the file
  console.log(data);
});
