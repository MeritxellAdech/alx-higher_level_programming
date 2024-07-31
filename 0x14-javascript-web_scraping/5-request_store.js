#!/usr/bin/node
const { argv } = require('process');
const { writeFile } = require('fs');
const request = require('request');

if (argv.length > 2) {
  const url = argv[2];
  request(url, (error, response, body) => {
    if (!error) {
      // write into the file
      writeFile(argv[3], body, 'utf-8', (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  });
}
