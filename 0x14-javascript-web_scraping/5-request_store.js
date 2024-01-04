#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let fs = require('fs');
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) { console.log(err); }
    });
  }
});
