#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args = require('process');
if (isNaN(args.argv[2]) || isNaN(args.argv[3])) {
  console.log('NaN');
} else {
  console.log(add(parseInt(args.argv[2]), parseInt(args.argv[3])));
}
