#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size) || size === undefined) {
  console.log("Missing size");
} else {
  const num = parseInt(size);
  for (let i = 0; i < num; i++) {
    let squareLine = '';
    for (let j = 0; j < num; j++) {
      squareLine += 'X';
    }
    console.log(squareLine);
  }
}
