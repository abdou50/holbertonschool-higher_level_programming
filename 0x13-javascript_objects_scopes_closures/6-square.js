#!/usr/bin/node
const rectangle = require('./4-rectangle');
class Square extends rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    let str = '';
    for (let i = 0; i < this.height; i++) {
      str += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(str);
    }
  }
}
module.exports = Square;
