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
      const userId = task.userId;
      if (task.completed) {
        if (userId in infoSet) {
          infoSet[userId] += 1;
        } else {
          infoSet[userId] = 1;
        }
      }
    });
    console.log(infoSet);
  }
});
