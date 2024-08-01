#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

if (argv.length > 2) {
  const url = argv[2];
  const obj = {};
  request(url, (error, response, body) => {
    if (!error) {
      for (const user of JSON.parse(body)) {
        if (user.completed) {
          obj[user.userId] = (obj[user.userId] ?? 0) + 1;
        }
      }
      console.log(obj);
    }
  });
}
