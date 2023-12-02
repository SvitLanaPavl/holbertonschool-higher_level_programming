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
      if (task.completed) {
        const userId = task.userID;
        infoSet[userId] = (infoSet[userId] || 0);
        infoSet[userId]++;
      }
    });
    Object.keys(infoSet).forEach(userId => {
      console.log(`${userId}: ${infoSet[userId]}`);
    });
  }
});
