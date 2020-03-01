// CLI usage: 
// java Binarysearch 29/1-3-5-7-9-12-14-15-17-18-19-22-25-27-29-35-36-38-45-47-49-51-55-57-59-62-64-65-67-68-69
//
// File usage:
// 29
// 1 3 5 7 9 12 14 15 17 18 19 22 25 27 29 35 36 38 45 47 49 51 55 57 59 62 64 65 67 68 69

//
// Simple client for Binarysearch to be used in Threesum
// Read a target, and an array of sorted ints
// Binary Search for the target
// Return the target's index in array if present
// Return -1 if not present
//

var file = require('/home/ubuntu/Dev/algs-ds/tools/file.js');
var cli = require('/home/ubuntu/Dev/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/6binarysearch1.txt'

class binarysearch { 
    constructor(target, list) {
        this.target = target;
        this.list = list;
    }

}

function runClient (inputs) {
    let target = inputs[0][0];
    let list = inputs[1];
    let bs = new binarysearch(target, list);

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