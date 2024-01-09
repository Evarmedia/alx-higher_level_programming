#!/usr/bin/node

// a function that returns the number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let ind = 0; ind < list.length; ind++) {
    if (list[ind] === searchElement) {
      counter++;
    }
  }
  return counter;
};
