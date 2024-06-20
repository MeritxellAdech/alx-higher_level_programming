#!/usr/bin/node

// Executes a function a given number of times
exports.callMeMoby = function (x, theFunction) {
  while (x >= 1) {
    theFunction();
    x--;
  }
};
