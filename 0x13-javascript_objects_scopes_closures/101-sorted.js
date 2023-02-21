#!/usr/bin/node

const dict = require('./101-data').dict;

const newD = {};
for (const k in dict) {
  if (newD[dict[k]] === undefined) {
    newD[dict[k]] = [];
  }
  newD[dict[k]].push(k);
}

console.log(newD);
