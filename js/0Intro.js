// CLI usage: 
// node 0Intro.js x-y-z/a-b-c
//
// File usage:
// x y z 
// a b c

var file = require('/home/ubuntu/Dev/algs-ds/tools/file.js');
var cli = require('/home/ubuntu/Dev/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/0intro3.txt'

if (process.argv.length > 2) {
   cli.readArgTo2DArray(process.argv[2], function (cliInput) {
        intro(cliInput);
   });

} else {
    file.readLinesTo2DArray(INPUT_FILE_PATH, function (fileInput) {
        intro(fileInput);
    });
}

function intro (inputs) {
    console.log('A.) Full 2D Array');
    console.log(inputs);
    console.log('B.) Each Row');
    inputs.map(i => {
        console.log(i);
    });
    console.log('C.) Each Cell');
    inputs.map(i => {
        i.map(j => {
            console.log(j);
        });
    })
}