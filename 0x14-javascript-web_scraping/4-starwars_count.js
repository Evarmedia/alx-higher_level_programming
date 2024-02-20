#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      if (films[i].characters.find((character) => character.endsWith('/18/'))) {
        count++;
      }
    }
    console.log(count);
  } else {
    console.error('An error occurred while fetching the movie count:', error);
  }
});
