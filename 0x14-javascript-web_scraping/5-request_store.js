#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(fileName, body, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
