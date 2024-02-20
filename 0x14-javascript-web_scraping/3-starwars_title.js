#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    console.log(film.title);
  } else {
    console.error('An error occurred while fetching the movie title:', error);
  }
});
