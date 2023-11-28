#!/usr/bin/node
exports.converter = function (base) {
  function convertToBase (number) {
    if (number < base) {
      return number.toString(base).toUpperCase();
    } else {
      return convertToBase(Math.floor(number / base)) +
      (number % base).toString(base).toUpperCase();
    }
  }
  return convertToBase;
};
