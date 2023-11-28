#!/usr/bin/node
if (parseInt(process.argv[2])) {
  const number = parseInt(process.argv[2]);
  for (let num = 0; num < number; num++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
