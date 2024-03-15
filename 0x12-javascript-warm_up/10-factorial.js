#!/usr/bin/node
const { argv } = require('node:process');
const number = parseInt(argv[2]);
function fac (n) {
  if (n === 0) {
    return 1;
  }
  return (n * fac(n - 1));
}
if (isNaN(number)) {
  console.log(1);
} else {
  console.log(fac(number));
}
