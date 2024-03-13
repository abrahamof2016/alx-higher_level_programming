#!/usr/bin/node
const { argv } = require('node:process');
const message = parseInt(argv[2]);
if (isNaN(message)) {
  console.log('Not a number');
} else {
  console.log('My number: ', message);
}
