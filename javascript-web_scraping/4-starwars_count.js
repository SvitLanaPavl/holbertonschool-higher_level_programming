#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const set of data) {
      for (const character of set.characters) {
        if (character.includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
