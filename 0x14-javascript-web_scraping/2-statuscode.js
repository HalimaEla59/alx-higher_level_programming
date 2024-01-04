#!/usr/bin/node
const adr = process.argv[2];
const request = require('request');
request.get(adr.on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
