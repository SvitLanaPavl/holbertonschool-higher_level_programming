#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const id = 18;
request(url, (error, _, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const data = JSON.parse(body).results;
      const films = data.filter((film) =>
        film.characters.includes(`https://swapi-api.hbtn.io/api/films/people/${id}/`));
      console.log(films.length);
    } catch (parseError) {
      console.error(parseError);
    }
  }
});
