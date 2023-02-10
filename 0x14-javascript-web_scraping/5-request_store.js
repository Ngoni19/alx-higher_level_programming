#!/usr/bin/node

let URL = process.argv[2];
let file_name = process.argv[3];
const fs = require('fs');
const request = require('request');

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file_name, body, 'utf8');
  }
});
