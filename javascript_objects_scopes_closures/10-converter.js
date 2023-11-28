#!/usr/bin/node
exports.converter = function (base) {
  function convertToBase (number) {
    let result = '';
    while (number > 0) {
      const remainder = number % base;
      number = Math.floor(number / base);
      result = remainder.toString() + result;
    }
    return result;
  }
  return convertToBase;
};
