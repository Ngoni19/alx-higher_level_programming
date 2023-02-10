#!/usr/bin/node

let url = process.argv[2];
const req = require('req');

req(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let d01 = {};
    let no_tasks = JSON.parse(body);
    for (let j in no_tasks) {
      if (no_tasks[j].completed) {
	if (d01[no_tasks[j].userId] === undefined) {
	  d01[no_tasks[j].userId] = 1;
	} else {
	  d01[no_tasks[j].userId]++;
	}
      }
    }
    console.log(d01);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
