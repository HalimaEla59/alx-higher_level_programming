#!/usr/bin/node
const n = process.argv[2];
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + n, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title));
  }
});
