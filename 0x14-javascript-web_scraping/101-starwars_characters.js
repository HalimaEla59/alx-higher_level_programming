#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com//api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let res = JSON.parse(body).characters;
    let promises = [];
    for (let i of res) {
      promises.push(new Promise(function (resolve, reject) {
        request(i, (e, r, b) => resolve(JSON.parse(b)['name']));
      }));
    }
    Promise.all(promises).then((a) => {
      for (let i of a) { console.log(i); }
    });
  }
});
