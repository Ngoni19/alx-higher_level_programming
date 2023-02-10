#!/usr/bin/node

let id = process.argv[2];
let URL = 'http://swapi.co/api/films/' + id;
const request = require('request');

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body['title']);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
