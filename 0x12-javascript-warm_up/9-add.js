#!/usr/bin/node
const { argv } = require('node:process');
function add (a, b) {
  const sum = Number(a) + Number(b);
  console.log(sum);
}
if (argv[2] === undefined | argv[3] === undefined) {
  console.log('NaN');
} else {
  add(argv[2], argv[3]);
}
