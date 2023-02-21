#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  for (const k in list) {
    if (list[k] === searchElement) {
      cnt++;
    }
  }
  return cnt;
};
