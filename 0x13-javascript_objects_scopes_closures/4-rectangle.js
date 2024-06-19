#!/usr/bin/node

/* Based on 2-rectangle - printing the shape */
module.exports = class Rectangle {
  constructor (w, h) {
    // creating an empty object if h or w is <= 0
    if ((w === undefined || h === undefined) || (w < 1 || h < 1)) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // print the rectangle
    const sign = 'X';
    for (let row = 0; row < this.height; row++) {
      console.log(sign.repeat(this.width));
    }
  }

  // rotate() method exchanges the width and the height of the rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // double() method multiples the width and the height of the rectangle by 2
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
