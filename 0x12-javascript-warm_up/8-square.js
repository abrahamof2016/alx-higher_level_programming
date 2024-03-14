#!/usr/bin/node
const { argv } = require('node:process');
const number = parseInt(argv[2]);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  let i = 0;
  let text = '';
  while (i < number) {
    let j = 0;
    while (j < number) {
      text = text.concat('X');
      j++;
    }
    console.log(text);
    text = '';
    i++;
  }
}
