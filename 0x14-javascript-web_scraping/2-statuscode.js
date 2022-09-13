#!/usr/bin/node
const axios = require('axios');
const process = require('process');
const arg = process.argv[2];
axios.get(arg)
  .then(function (response) {
    console.log(`code: ${response.status}`);
  })
  .catch(function (err) {
    console.log(`code: ${err.response.status}`);
  });
