#!/usr/bin/node
const file = process.argv[2];
const str = process.argv[3];
const fs = require('fs');
fs.writeFile(file, str, error => {
  if (error) console.log(error);
});
