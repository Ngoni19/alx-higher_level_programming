#!/usr/bin/node

exports.esrever = function (list) {
  let b = 0;
  let e = list.length - 1;
  while (b < e) {
    const tmp = list[b];
    list[b] = list[e];
    list[e] = tmp;
    b++;
    e--;
  }
  return list;
};
