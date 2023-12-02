#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fs = require('fs');
const filepath = process.argv[3];
request(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFileSync(filepath, body, 'utf8');
  }
});
