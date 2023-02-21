#!/usr/bin/node

let fA = process.argv[2];
let fB = process.argv[3];
let fC = process.argv[4];
const fs = require('fs');
let txtA = fs.readFileSync(fA, 'utf8');
let txtB = fs.readFileSync(fB, 'utf8');
fs.writeFileSync(fC, txtA + txtB);
