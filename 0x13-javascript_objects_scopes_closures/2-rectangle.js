#!/usr/bin/node

// Referencing 1-rectangle file, create an empty object if 'w' or 'h' are <= 0
module.exports = class Rectangle {
  constructor (w, h) {
    // creating an empty object if h or w is <= 0
    if ((w === undefined || h === undefined) || (w < 1 || h < 1)) {
      return;
    }
    this.width = w;
    this.height = h;
  }
};
