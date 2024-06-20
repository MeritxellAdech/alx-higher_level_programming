#!/usr/bin/node
const { readFile, writeFile } = require('fs').promises;
const { argv } = require('process');

[argv[2], argv[3]].forEach((file) => {
  readFile(file).then((content) => writeFile(argv[4], content, { flag: 'a' }));
});
