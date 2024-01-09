#!/usr/bin/node

// a script that imports a dict by userid and computes a dict of uid by occurrences.
const { dict } = require('./101-data');

const usersByOccurrence = Object.entries(dict).reduce((acc, [userId, occurrences]) => {
  if (acc[occurrences]) {
    acc[occurrences].push(userId);
  } else {
    acc[occurrences] = [userId];
  }
  return acc;
}, {});

console.log(usersByOccurrence);
