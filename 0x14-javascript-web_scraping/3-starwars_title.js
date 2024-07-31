#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
// get the code
request(url, (error, response) => {
  if (!error) {
    const res = response.body;
    console.log(JSON.parse(res).title);
  }
});
