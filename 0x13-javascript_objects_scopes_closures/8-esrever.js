#!/usr/bin/node
exports.esrever = function (list) {
  const reversedL = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedL.push(list[i]);
  }
  return reversedL;
};
