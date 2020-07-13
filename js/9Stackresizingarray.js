// CLI usage: 
// node js/9stacklinkedlist.js 1-2-3-777-4-5-6-777-777-777
//
// File usage:
// 1 2 3 777 4 5 6 777 777 777

//
// Stack of ints implemented by linked list
// ints in input stream will be pushed onto stack
// input of 777 will print popped int from stack
//

var onUbuntu = true;

var baseDevFolder = onUbuntu 
    ? '/home/ubuntu/Dev'
    : '/Users/brianfoster/dev';

var file = require(baseDevFolder + '/algs-ds/tools/file.js');
var cli = require(baseDevFolder + '/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = baseDevFolder + '/algs-ds/input/9stack2.txt';

class stackresizingarray { 

    constructor() {
        this.stackArray = new Array(1);
        this.N = 0;
    }

    push(item) {
        if (this.N === this.stackArray.length) {
            this.resize(2 * this.stackArray.length);
        }
        this.stackArray[this.N++] = item;
    }

    pop() {
        if (this.N > 0 && this.N == (this.stackArray.length / 4)) {
            this.resize(this.stackArray.length /2);
        }
        return this.stackArray[--this.N];
    }

    isEmpty() {
        return this.N == 0;
    }

    resize(capacity) {
        let copyArray = new Array(capacity);
        for (let i = 0; i < this.N; i++) {
            copyArray[i] = this.stackArray[i];
        }
        this.stackArray = copyArray;
    }

    size() {
        return this.N;
    }

    stackValues() {
        if (this.isEmpty() || this.size() == 0) {
            return new [];
        } else {
            let stackValues = new Array(this.size());
            for (let i = 0; i < this.N; i++) {
                stackValues[i] = this.stackArray[i];
            }
            return stackValues;
        }
    }
}

//
// CLIENT
//


function runClient (inputs) {

    let sra = new stackresizingarray();

    inputs[0].forEach(function (item) {
        if (item == 777) {
            console.log("Popped from stack: " + sra.pop());
            console.log("Stack size: " + sra.size());
        } else {
            sra.push(item);
            console.log("Pushed on: " + item);
            console.log("Stack size: " + sra.size());
        }
    });
        
    let finalSize = sra.size();
    if (finalSize > 0) {
        console.log("Final stack (last-first/top-bottom/newest-oldest):");
        console.log(sra.stackValues());
    } else if (sra.isEmpty()) {
        console.log("Final stack is empty.");
    } else {
        console.log("Error? final size and isEmpty don't agree.");
    }
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