#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string = '';
    for (let i = 0; i < this.width; i++) {
      string += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(string);
    }
  }
}
module.exports = Rectangle;
