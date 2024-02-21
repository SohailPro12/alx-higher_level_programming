#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';

let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    for (const film of films) {
      const characters = film.characters;
      for (const characterUrl of characters) {
        const id = characterUrl.split('/').slice(-2, -1)[0];
        if (id === characterId) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
