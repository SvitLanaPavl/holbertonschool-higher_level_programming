#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, (error, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      console.log(JSON.parse(body).title);
    } catch (parseError) {
      console.error(parseError);
    }
    
  }
});
