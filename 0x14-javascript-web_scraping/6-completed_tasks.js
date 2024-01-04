#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let results = {};
    for (let tod of JSON.parse(body)) {
      if (tod.completed) {
        if (results[tod['userId']] === undefined) { results[tod['userId']] = 0; }
        results[tod['userId']] += 1;
      }
    }
    console.log(results);
  }
});
