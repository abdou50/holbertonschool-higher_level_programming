#!/usr/bin/node
function factorial (x) {
  if (x === 0 || x === 1 || isNaN(x)) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
const process = require('process');
const x = process.argv[2];
console.log(factorial(x));
