// CLI usage: node 0Intro.js x,y,z,a,b,c
var file = require('../tools/file.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/test1.txt'

if (process.argv.length > 2) {
    let arrayArgument = process.argv[2].split(',');
    let arraySum = arrayArgument.reduce((a,b) => parseInt(a, 10) + parseInt(b, 10), 0);
    console.log(arrayArgument);
    console.log('your array sum is:');
    console.log(arraySum);
} else {
    file.readLinesToArray(INPUT_FILE_PATH, function (inputs) {
        intro(inputs);
    });
}

function intro (inputs) {
    console.log(inputs);
    inputs.map( i => {
        i.map(j => {
            console.log(j);
            })
    });
}

