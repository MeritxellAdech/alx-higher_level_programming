#!/usr/bin/node

// Anonymous function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  for (const i of list) {
    if (i === searchElement) {
      occ++;
    }
  }
  return (occ);
};
