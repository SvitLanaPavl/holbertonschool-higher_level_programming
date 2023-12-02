#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const infoSet = {};
    tasks.forEach(task => {
      const userId = task.userID;
      if (task.completed && infoSet[userId] === undefined) {
        infoSet[userId] = 0;
      } else if (task.completed) {
        infoSet[userId] += 1;
      }
    });
    console.log(infoSet);
  }
});
