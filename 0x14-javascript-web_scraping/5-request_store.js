#!/usr/bin/node

let url = process.argv[2];
let file_name = process.argv[3];
const fs = require('fs');
const req = require('req');

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file_name, body, 'utf8');
  }
});
