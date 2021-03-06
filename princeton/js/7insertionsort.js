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

var file = require('/home/ubuntu/Dev/algs-ds/tools/file.js');
var cli = require('/home/ubuntu/Dev/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/7insertionsort1.txt'

class insertionsort { 
    constructor(list) {
        this.list = list;
    }

    sort(list) {
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

module.exports = insertionsort

// function runClient (inputs) {
//     let list = inputs[0];
    
//     console.log("Unsorted list:");
//     console.log(list);

//     let is = new insertionsort();
//     is.sort(list);

//     console.log("Sorted list:");
//     console.log(list);
// }

// if (process.argv.length > 2) {
//     cli.readArgTo2DArray(process.argv[2], function (cliInput) {
//          runClient(cliInput);
//     });
 
//  } else {
//      file.readLinesTo2DArray(INPUT_FILE_PATH, function (fileInput) {
//          runClient(fileInput);
//      });
//  }