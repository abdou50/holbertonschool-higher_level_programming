#!/usr/bin/node
const axios = require('axios');
const process = require('process');
const arg = process.argv[2];
axios.get('https://swapi-api.hbtn.io/api/films/')
	.then(function (response) {
		console.log(response.data.results[arg].title);
	})
	.catch(function (err) {
		console.log(err);
	});
