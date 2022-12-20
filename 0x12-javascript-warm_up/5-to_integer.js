#!/usr/bin/node

const Arg_Num = parseInt(process.argv[2], 10);
if (isNaN(Arg_Num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Arg_Num}`);
}
