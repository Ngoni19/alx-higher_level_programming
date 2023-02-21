#!/usr/bin/node

const dict = require('./101-data').dict;

let newD = {};
for (let k in dict) {
  if (newD[dict[k]] === undefined) {
    newD[dict[k]] = [];
  }
  newD[dict[k]].push(k);
}

console.log(newD);
