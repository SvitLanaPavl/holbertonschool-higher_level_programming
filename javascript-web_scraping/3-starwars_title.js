#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, (error, jsonData) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(jsonData).title);
  }
});
