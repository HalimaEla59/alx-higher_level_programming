#!/usr/bin/node
const s = process.argv[2];
if (isNaN(Number(s))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(s); i++) {
    console.log('C is fun');
  }
}
