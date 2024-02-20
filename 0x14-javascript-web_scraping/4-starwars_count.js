#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const { results } = JSON.parse(body);
    const moviesWithWedgeAntilles = results.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(moviesWithWedgeAntilles.length);
  } else {
    console.error('An error occurred while fetching the movie count:', error);
  }
});
