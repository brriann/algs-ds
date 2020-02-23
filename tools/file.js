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

