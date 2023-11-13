#!/usr/bin/node
const s = process.argv[2];
if (isNaN(Number(s))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(s); i++) {
    console.log('X'.repeat(s));
  }
}
