#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      const characters = film.characters;
      for (const character of characters) {
        if (character === 'https://swapi-api.alx-tools.com/api/people/18') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
