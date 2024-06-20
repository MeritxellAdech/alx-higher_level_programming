#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  if (number) {
    theFunction(++number);
  }
};
