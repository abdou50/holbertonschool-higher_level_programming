#!/usr/bin/node
const fs = require('fs');
const arg = process.argv[2];
const arg2 = process.argv[3];
fs.writeFile(arg, arg2, function (err) {
  if (err) throw err;
});
