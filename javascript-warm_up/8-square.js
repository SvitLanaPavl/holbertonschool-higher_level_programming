#!/usr/bin/node
if (parseInt(process.argv[2])) {
  const number = parseInt(process.argv[2]);
  for (let num = 0; num < number; num++) {
    let row = '';
    for (let n = 0; n < number; n++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
