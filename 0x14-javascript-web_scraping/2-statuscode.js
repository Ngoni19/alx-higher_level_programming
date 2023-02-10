#!/usr/bin/node

let URL = process.argv[2];
const request = require('request');

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
