#!/usr/bin/node
exports.converter = function (base) {
  return function (num) {
    return parseInt(num).toString(base);
  };
};
