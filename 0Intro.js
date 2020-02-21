// invoke this script with an int array from CLI as "node 0Intro.js 0,1,2,3,4"

/* if (process.argv.length < 3) {
    console.log('usage: node 0Intro.js x,y,z,a,b,c');
} else {
    let arrayArgument = process.argv[2].split(',');
    let arraySum = arrayArgument.reduce((a,b) => parseInt(a, 10) + parseInt(b, 10), 0);
    console.log(arrayArgument);
    console.log('your array sum is:');
    console.log(arraySum);

} */

const fs = require('fs');
const readline = require('readline');


var inputs = [];

const rl = readline.createInterface({
  input: fs.createReadStream('test2.txt'),
  crlfDelay: Infinity
});

rl.on('line', (line) => {
    var lineArray = [];
    var strings = line.split(' ');
    for (var i = 0; i < strings.length; i++) {
        lineArray.push(Number(strings[i]));
    }
  inputs.push(lineArray);
  console.log(`Line from file: ${line}`);
}).on('close', () => {
    console.log(inputs);
});

