#!/usr/bin/node

let i = 0;
// Prints the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  console.log(`${i++}: ${item}`);
};
