#!/usr/bin/node
exports.esrever = function (arr) {
  const n = arr.length - 1;

  for (let i = 0; i <= n / 2; i++) {
    const temp = arr[i];
    arr[i] = arr[n - i];
    arr[n - i] = temp;
  }
  return arr;
};
