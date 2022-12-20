#!/usr/bin/node

const Size = parseInt(process.argv[2], 10);
if (isNaN(Size)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < Size; j += 1) {
    console.log('X'.repeat(Size));
  }
}
