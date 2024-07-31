#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

// get the code
request(argv[2], (error, response) => {
  if (!error) {
    console.log('code:', response.statusCode);
  }
});
