#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const maxNum = Math.max(...args);
  const lowerNums = args.filter(num => num < maxNum);
  const secondMax = Math.max(...lowerNums);
  console.log(secondMax);
}
