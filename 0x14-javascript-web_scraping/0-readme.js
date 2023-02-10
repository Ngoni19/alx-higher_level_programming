#!/usr/bin/node

let file_name = process.argv[2];
const fs = require('fs');
fs.readFile(file_name, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
