#!/usr/bin/node
const process = require('process');
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My mumber: ' + parseInt(process.argv[2]));
}
