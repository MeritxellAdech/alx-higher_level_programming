#!/usr/bin/node
const request = require('request');
const { argv } = require('process');

if (argv.length > 2) {
  const url = argv[2];
  let total = 0;
  // get the code
  request(url, (error, response) => {
    if (!error) {
      // get all the response
      const data = JSON.parse(response.body);
      const { results } = data;
      for (const movie of results) {
        // get the list of characters
        const { characters } = movie;
        for (const actor of characters) {
          // loop through the characters to find the one with id=18
          if (actor.includes(18)) {
            total++;
          }
        }
      }
      console.log(total);
    }
  });
}
