#!/usr/bin/node

const fA = process.argv[2];
const fB = process.argv[3];
const fC = process.argv[4];
const fs = require('fs');
const txtA = fs.readFileSync(fA, 'utf8');
const txtB = fs.readFileSync(fB, 'utf8');
fs.writeFileSync(fC, txtA + txtB);
