// CLI usage: 
// java Insertionsort 1-3-5-7-9-12-14-15-17-18-19-22-25-27-29-35-36-38-45-47-49-51-55-57-59-62-64-65-67-68-69
//
// File usage:
// 1 3 5 7 9 12 14 15 17 18 19 22 25 27 29 35 36 38 45 47 49 51 55 57 59 62 64 65 67 68 69

//
// Simple client for Insertion Sort to be used in Threesum
// Read an array of ints
// Sort using Insertion Sort
// Return sorted list
//

var onUbuntu = false;

var baseDevFolder = onUbuntu 
    ? '/home/ubuntu/Dev'
    : '/Users/brianfoster/dev';

var file = require(baseDevFolder + '/algs-ds/tools/file.js');
var cli = require(baseDevFolder + '/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = baseDevFolder + '/algs-ds/input/7insertionsort1.txt';

class insertionsort2 { 
    constructor() {
    }

    less(v, w) {
        // only handling int's for now, may do -1/0/1 comparators in the future for other types
        return v < w;
    }

    exchange(array, i, j) {
        var swap = array[i];
        array[i] = array[j];
        array[j] = swap;
    }

    newSort(list) {
        for (let i = 0; i < list.length; i++) {
            for (let j = i; j > 0; j--) {
                if (this.less(list[j], list[j - 1])) {
                    this.exchange(list, j, j - 1);
                } else {
                    break;
                }
            }
        }
    }

    // old implemenation for comparison
    // see 7insertionsort.js
    oldSort(list) {
        for (let i = 1; i < list.length; i++) {
            let j = i - 1;
            let temp = list[i];
            while (j >= 0 && list[j] > temp) {
                list[j + 1] = list[j]
                j -= 1;
            }
            list[j + 1] = temp
        }
    }
}



//
// CLIENT
//


function runClient (inputs) {
    let list = inputs[0];
    
    console.log("Unsorted list:");
    console.log(list);

    let is = new insertionsort2();
    is.newSort(list);

    console.log("Sorted list:");
    console.log(list);
}

if (process.argv.length > 2) {
    cli.readArgTo2DArray(process.argv[2], function (cliInput) {
         runClient(cliInput);
    });
 
 } else {
     file.readLinesTo2DArray(INPUT_FILE_PATH, function (fileInput) {
         runClient(fileInput);
     });
 }