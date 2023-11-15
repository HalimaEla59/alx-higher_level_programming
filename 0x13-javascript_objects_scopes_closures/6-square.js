#!/usr/bin/node
const SquareFive = require('./5-square');

class Square extends SquareFive {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
