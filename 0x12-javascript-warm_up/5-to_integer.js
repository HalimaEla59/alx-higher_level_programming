#!/usr/bin/node
let s = process.argv.slice(2);
if (isNaN(Number(s[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(s[0]));
}
