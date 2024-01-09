#!/usr/bin/node 

//a function that reveres an array(list)

exports.esrever = function (list) {
  const newList = []
  for (let i = list.length-1; i >= 0; i--) {
    newList.push(list[i])
  }
  return newList;
};
