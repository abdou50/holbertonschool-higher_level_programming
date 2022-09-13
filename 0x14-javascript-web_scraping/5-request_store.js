#!/usr/bin/node
const axios = require('axios');
const process = require('process');
const fs = require('fs');
const arg = process.argv[2];
const arg1 = process.argv[3];
axios.get(arg)
  .then(function (response) {
    fs.writeFile(arg1, response.data, function (err) {
      if (err) throw err;
    });
  });
