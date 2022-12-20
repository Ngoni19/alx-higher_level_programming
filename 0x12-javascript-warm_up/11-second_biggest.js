#!/usr/bin/node

const NumArr = process.argv.slice(2);
function secondMax (arr) {
  if (arr.length < 2) {
    return (0);
  } else {
    arr.sort((j, k) => j - k);
    arr.pop();
    return (arr.pop());
  }
}
console.log(secondMax(NumArr));
