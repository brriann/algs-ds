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

var file = require('/Users/brianfoster/dev/algs-ds/tools/file.js');
var cli = require('/Users/brianfoster/dev/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/9stack2.txt';
const INPUT_FILE_PATH_2 = '/Users/brianfoster/dev/algs-ds/input/9stack2.txt';

class queuelinkedlist { 

    constructor() {
        this.firstNode = null;
        this.lastNode = null;
    }

    enQueue(item) {
        let oldLastNode = this.lastNode;
        this.lastNode = new node(item, null);
        if (this.isEmpty()) {
            this.firstNode = this.lastNode;
        } else {
            oldLastNode.nextNode = this.lastNode;
        }
    }

    deQueue() {
        let item = this.firstNode.item;
        this.firstNode = this.firstNode.nextNode;
        if (this.isEmpty()) {
            this.lastNode = null;
        }
        return item;
    }

    isEmpty() {
        return this.firstNode == null;
    }

    size() {
        let sizeTracker = 0;
        let nodeTracker = this.firstNode;
        while (nodeTracker != null) {
            sizeTracker++;
            nodeTracker = nodeTracker.nextNode;
        }
        return sizeTracker;
    }

    queueValues() {
        if (this.isEmpty() || this.size() == 0) {
            return new [];
        } else {
            let queueValues = [];
            let index = 0;
            let nodeTracker = this.firstNode;

            while (nodeTracker != null) {
                queueValues[index++] = nodeTracker.item;
                nodeTracker = nodeTracker.nextNode;
            }
            return queueValues;
        }
    }
}

class node {
    constructor (item, nextNode) {
        this.item = item;
        this.nextNode = nextNode;
    }   
}


//
// CLIENT
//


function runClient (inputs) {

    let qll = new queuelinkedlist();

    inputs[0].forEach(function (item) {
        if (item == 777) {
            console.log("dequeued from queue: " + qll.deQueue());
            console.log("queue size: " + qll.size());
        } else {
            qll.enQueue(item);
            console.log("enqueued: " + item);
            console.log("queue size: " + qll.size());
        }
    });
        
    let finalSize = qll.size();
    if (finalSize > 0) {
        console.log("Final queue (last-first/top-bottom/newest-oldest):");
        console.log(qll.queueValues());
    } else if (qll.isEmpty()) {
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
     file.readLinesTo2DArray(INPUT_FILE_PATH_2, function (fileInput) {
         runClient(fileInput);
     });
 }