// CLI usage: 
// node 8threesumopt.js 4 -4 2 6 0 -2 8 10 -6 ( WILL NOT USE CLI)
//
// File usage:
//4 -4 2 6 0 -2 8 10 -6

//
// Optimized implementation of three-sum
// Read an array of ints - Identify all triples that sum to zero
// Sort the list
// for each pair of numbers a[i] and a[j], binary search for -(a[i] + a[j])
//

var file = require('/home/ubuntu/Dev/algs-ds/tools/file.js');
var cli = require('/home/ubuntu/Dev/algs-ds/tools/cli.js');
var binarysearch = require('/home/ubuntu/Dev/algs-ds/js/6binarysearch.js');
var insertionsort = require('/home/ubuntu/Dev/algs-ds/js/7insertionsort.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/8threesum3.txt'

class threesumopt { 
    constructor(list) {
        this.iSort = new insertionsort();
        this.bSearch = new binarysearch();

        this.foundTriples = [];
    }

    storeFoundTriples(triple) {

    }

    threesum(list) {
        console.log('input list: ');
        console.log(list);

        this.iSort.sort(list);

        console.log('sorted list: ');
        console.log(list);

        let n = list.length;
        let count = 0;

        for (let i = 0; i < n; i++) {
            for (let j = i + 1; j < n; j++) {
                let ij = -(list[i] + list[j]);
                let indexIj = this.bSearch.search(0, n - 1, ij, list);
                if (indexIj >= 0 && list[i] < list[j] && list[j] < ij) {
                    console.log('3-SUM: ' + list[i] + ' ' + list[j] + ' ' + ij); // ij = list[indexIj] = list[i] + list[j]
                    count += 1;
                    this.foundTriples.push([list[i], list[j], ij])
                }
            }
        }
        console.log('*** 3- SUM RESULTS ***');
        console.log('count: ' + count);
        console.log('Found Triples:');
        console.log(this.foundTriples);
    }
}

function runClient (inputs) {
    let list = inputs[0];

    let tso = new threesumopt();
    tso.threesum(list);
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