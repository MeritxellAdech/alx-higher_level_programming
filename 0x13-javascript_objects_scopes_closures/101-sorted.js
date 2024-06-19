#!/usr/bin/node
const { dict } = require('./101-data.js');

const newDict = {};
// Groups the value with all its keys
for (const [key, value] of Object.entries(dict)) {
  newDict[value] === undefined ? newDict[value] = [key] : newDict[value].push(key);
}
console.log(newDict);
