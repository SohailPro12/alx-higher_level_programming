#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    body = JSON.parse(body);
    const completedTasksByUsers = {};
    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed) {
        if (completedTasksByUsers[userId]) {
          completedTasksByUsers[userId]++;
        } else {
          completedTasksByUsers[userId] = 0;
        }
      }
    }

    console.log(completedTasksByUsers);
  }
});
