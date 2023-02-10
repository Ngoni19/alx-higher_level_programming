#!/usr/bin/node

let file_name = process.argv[2];
let txt = process.argv[3];
const fs = require('fs');
fs.writeFile(file_name, txt, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
