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

    search(low, middle, high) {
        while (this.list[middle] != this.target) {
            // TODO: continue here for JS
        }
    }

}

function runClient (inputs) {
    let targetin = inputs[0][0];
    let listin = inputs[1];
    let bs = new binarysearch(targetin, listin);

    let initialLow = 0;
    let initialMiddle = parseInt(listin.length / 2);
    initialHigh = (listin.length - 1);

    console.log('initial lo mi hi: ' + initialLow + ' ' + initialMiddle + ' ' + initialHigh);
    let targetIndex = bs.search(initialLow, initialMiddle, initialHigh)

    if (targetIndex < 0) {
        console.log('*** TARGET NOT IN LIST ***')
    } else {
        console.log('*** TARGET ' + targetin + ' FOUND AT INDEX ' + targetIndex + ' IN LIST  ' + listin)
    }
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