#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com//api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let charact = JSON.parse(body).characters;
    for (let i of charact) {
      request(i, (e, r, b) => console.log(JSON.parse(b)['name']));
    }
  }
});
