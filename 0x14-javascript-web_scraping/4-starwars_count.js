#!/usr/bin/node
const axios = require('axios');
const process = require('process');
const arg = process.argv[2];
let o = 0;
axios.get(arg)

  .then(function (response) {
    for (let i = 0; i < response.data.count; i++) {
      if (String(response.data.results[i].characters).includes('18')) {
        o += 1;
      }
    }
    console.log(o);
  })
  .catch(function (err) {
    console.log(err);
  });
