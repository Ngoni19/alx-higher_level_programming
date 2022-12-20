#!/usr/bin/node

const ArgNum = parseInt(process.argv[2], 10);
if (isNaN(ArgNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${ArgNum}`);
}
