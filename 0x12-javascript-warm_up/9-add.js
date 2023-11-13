#!/usr/bin/node
const x = process.argv[2];
const y = process.argv[3];
function add (a, b) {
  return (a + b);
}

console.log(add(Number(x), Number(y)));
