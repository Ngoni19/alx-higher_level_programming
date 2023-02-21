#!/usr/bin/node
const BaseSquare = require('./5-square');

module.exports = class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 0; x < this.width; x += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
