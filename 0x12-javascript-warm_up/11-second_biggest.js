#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      max = process.argv[i];
    }
  }
  max--;
  for (let i = 2; i < process.argv.length; i++) {
    if (process.argv[i] < max) {
      break;
    }
  }
  console.log(max);
}
