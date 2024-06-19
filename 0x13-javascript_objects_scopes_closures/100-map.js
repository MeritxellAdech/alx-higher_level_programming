#!/usr/bin/node
const list = require('./100-data.js').list;

// A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
let i = 0;
const newList = list.map((x) => x * i++);

console.log(list);
console.log(newList);
