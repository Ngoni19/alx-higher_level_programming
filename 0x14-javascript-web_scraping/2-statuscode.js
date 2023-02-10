#!/usr/bin/node

let url = process.argv[2];
const req = require('req');

req(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
