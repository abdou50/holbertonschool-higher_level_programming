#!/usr/bin/node
const process = require('process');
let str = '';
if (process.argv[2]) {
  for (let i = 0; i < process.argv[2]; i++) {
    str += 'X';
  }
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(str);
  }
} else if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
