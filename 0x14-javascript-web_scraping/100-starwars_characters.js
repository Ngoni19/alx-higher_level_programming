#!/usr/bin/node

let movie_id = process.argv[2];
let url = 'http://swapi.co/api/films/' + movie_id;
const req = require('req');

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    for (let j in body.characters) {
      req(body.characters[j], function (err, response, body) {
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
