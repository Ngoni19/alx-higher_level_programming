#!/usr/bin/node

let movie_id = process.argv[2];
let URL = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;
const request = require('request');

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    for (let j in body.characters) {
      request(body.characters[j], function (err, response, body) {
	if (err) {
	  console.log(err);
	} else if (response.statusCode === 200) {
	  console.log(JSON.parse(body).name);
	}
      });
    }
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
