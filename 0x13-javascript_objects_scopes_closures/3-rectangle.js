#!/usr/bin/node

// a class that defines a rectangle(with an instance that prints x)

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        let theRow = '';
        for (let k = 0; k < this.width; k++) {
          theRow += 'X';
        }
        console.log(theRow);
      }
    }
  }
}

module.exports = Rectangle;
