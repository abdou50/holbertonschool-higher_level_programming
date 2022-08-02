#!/usr/bin/node
exports.converter = function (base) {
  function converttoany (n) {
    return (n.toString(base));
  }
  return converttoany;
};
