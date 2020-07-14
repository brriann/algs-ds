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

var onUbuntu = false;

var baseDevFolder = onUbuntu 
    ? '/home/ubuntu/Dev'
    : '/Users/brianfoster/dev';

var file = require(baseDevFolder + '/algs-ds/tools/file.js');
var cli = require(baseDevFolder + '/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = baseDevFolder + '/algs-ds/input/9stack1.txt';

class queueresizingarray { 

    constructor() {
        this.queueArray = new Array(1);
        this.N = 0;
        this.first = 0;
        this.last = 0;
    }

    enQueue(item) {
        if (this.N === this.queueArray.length) {
            this.resize(2 * this.queueArray.length);
        }
        this.queueArray[this.last++] = item;
        if (this.last === this.queueArray.length) {
            this.last = 0;
        }
        this.N++;
    }

    deQueue() {
        let item = this.queueArray[this.first];
        this.queueArray[this.first] = null;
        this.N--;
        this.first++;
        if (this.first === this.queueArray.length) {
            this.first = 0;
        }
        if (this.N > 0 && this.N === this.queueArray.length / 4) {
            this.resize(this.queueArray.length / 2);
        }
        return item;
    }

    isEmpty() {
        return this.N === 0;
    }

    resize(capacity) {
        if (capacity >= this.N) {
            let copyArray = new Array(capacity);
            for (let i = 0; i < this.N; i++) {
                copyArray[i] = this.queueArray[(this.first + i) % this.queueArray.length];
            }
            this.queueArray = copyArray;
            this.first = 0;
            this.last = this.N;
        }
    }

    size() {
        return this.N;
    }

    queueValues() {
        if (this.isEmpty() || this.size() == 0) {
            return new [];
        } else {
            let queueValues = new Array(this.size());
            for (let i = 0; i < this.N; i++) {
                queueValues[i] = this.queueArray[(this.first + i) % this.queueArray.length];
            }
            return queueValues;
        }
    }
}


//
// CLIENT
//


function runClient (inputs) {

    let qra = new queueresizingarray();

    inputs[0].forEach(function (item) {
        if (item == 777) {
            console.log("dequeued from queue: " + qra.deQueue());
            console.log("queue size: " + qra.size());
        } else {
            qra.enQueue(item);
            console.log("enqueued: " + item);
            console.log("queue size: " + qra.size());
        }
    });
        
    let finalSize = qra.size();
    if (finalSize > 0) {
        console.log("Final queue (last-first/top-bottom/newest-oldest):");
        console.log(qra.queueValues());
    } else if (qra.isEmpty()) {
        console.log("Final queue is empty.");
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