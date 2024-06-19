#!/usr/bin/node

// Anonymous function that returns the reversed version of a list
exports.esrever = function (list) {
  const reversed = [];
  let rev = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    reversed[i] = list[rev--];
  }
  return (reversed);
};
