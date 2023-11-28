#!/usr/bin/node
function fact (n) {
  if (n === 1) {
    return 1;
  }
  return n * fact(n - 1);
}
const number = parseInt(process.argv[2]);
if (number) {
  console.log(fact(number));
} else {
  console.log(1);
}
