#!/usr/bin/node

let URL = process.argv[2];
const request = require('request');

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let filmz = JSON.parse(body).results;
    let cnt = 0;
    for (let j in filmz) {
      let chars = filmz[j].characters;
      for (let c in chars) {
	if (chars[c].includes('18')) {
	  cnt++;
	}
      }
    }
    console.log(cnt);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
