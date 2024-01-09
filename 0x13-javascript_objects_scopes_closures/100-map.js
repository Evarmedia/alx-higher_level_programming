#!/usr/bin/node

// script that imports an array and computes a new array

const { list } = require('./100-data');

const newArray = list.map((element, index) => element * index);

console.log(list);
console.log(newArray);
