#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const data = JSON.parse(body);
      console.log(data.title);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
