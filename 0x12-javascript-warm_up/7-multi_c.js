#!/usr/bin/node

const Num = parseInt(process.argv[2], 10);
if (isNaN(Num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = Num; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
