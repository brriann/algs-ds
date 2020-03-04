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

    search(low, high) {
        let foundIndex = -1;
        let found = false;

        while (low <= high && !found) {
            let middle = parseInt(low + ((high-low) / 2));
            console.log('SEARCH lo hi: ' + low + ' ' + high);
            console.log('cald\'d mid: ' + middle);

            if (this.list[middle] > this.target) {
                console.log('go lower');
                high = middle - 1;
            } else if (this.list[middle] < this.target) {
                console.log('go higher');
                low = middle + 1;
            } else  {
                foundIndex = middle;
                found = true;
            }
        }
        return foundIndex;
    }

}

function runClient (inputs) {
    let targetin = inputs[0][0];
    let listin = inputs[1];

    let bs = new binarysearch(targetin, listin);

    let initialLow = 0;
    let initialHigh = (listin.length - 1);

    console.log('initial lo hi: ' + initialLow + ' ' + initialHigh);
    let targetIndex = bs.search(initialLow, initialHigh)

    // targetIndex = -1 for Not Found
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