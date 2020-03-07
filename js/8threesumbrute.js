// CLI usage: 
// node 8threesumbrute.js 4 -4 2 6 0 -2 8 10 -6 ( WILL NOT USE CLI)
//
// File usage:
//4 -4 2 6 0 -2 8 10 -6

//
// Brute force implementation of Three-sum
// Read an array of ints
// Identify all triples that sum to zero
//

var file = require('/home/ubuntu/Dev/algs-ds/tools/file.js');
var cli = require('/home/ubuntu/Dev/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/8threesum3.txt'

class threesumbrute { 
    constructor(list) {
        this.list = list;
    }

    threesum(list) {
        let n = list.length;
        let count = 0;
        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                for (let k = j + 1; k < n; k++) {
                    if (list[i] + list[j] + list[k] === 0) {
                        console.log('3-SUM: ' + list[i] + ' ' + list[j] + ' ' + list[k]);
                        count += 1;
                    }
                }
            }
        }
        console.log('count: ' + count);
    }
}

function runClient (inputs) {
    let list = inputs[0];

    let tsb = new threesumbrute();
    tsb.threesum(list);
}

//
// CLIENT
//

if (process.argv.length > 2) {
    cli.readArgTo2DArray(process.argv[2], function (cliInput) {
         runClient(cliInput);
    });
 
 } else {
     file.readLinesTo2DArray(INPUT_FILE_PATH, function (fileInput) {
         runClient(fileInput);
     });
 }