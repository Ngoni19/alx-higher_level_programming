#!/usr/bin/node

let URL = process.argv[2];
const request = require('request');

request(URL, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let dict = {};
    let no_tasks = JSON.parse(body);
    for (let j in no_tasks) {
      if (no_tasks[j].completed) {
	if (dict[no_tasks[j].userId] === undefined) {
	  dict[no_tasks[j].userId] = 1;
	} else {
	  dict[no_tasks[j].userId]++;
	}
      }
    }
    console.log(dict);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
