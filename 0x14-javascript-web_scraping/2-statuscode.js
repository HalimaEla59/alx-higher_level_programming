#!/usr/bin/node
const addr = process.argv[2];
const request = require('request');
request(addr, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response['statusCode']);
  }
});
