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

  rotate () {
    const ttmp = this.width;
    this.width = this.height;
    this.height = ttmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
