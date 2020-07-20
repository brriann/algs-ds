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

class stacklinkedlist { 

    constructor() {
        this.firstNode = null;
    }

    push(item) {
        let oldFirstNode = this.firstNode;
        this.firstNode = new node(item, oldFirstNode);
    }

    pop() {
        let item = this.firstNode.item;
        this.firstNode = this.firstNode.nextNode;
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

    stackValues() {
        if (this.isEmpty() || this.size() == 0) {
            return new [];
        } else {
            let stackValues = [];
            let index = 0;
            let nodeTracker = this.firstNode;

            while (nodeTracker != null) {
                stackValues[index++] = nodeTracker.item;
                nodeTracker = nodeTracker.nextNode;
            }
            return stackValues;
        }
    }

    hasNext() {
        // currentNode would be assigned at instantiation of iterator, not inside this function
        var currentNode = this.firstNode;
        return currentNode != null;
    }

    next() {
        // currentNode would be assigned at instantiation of iterator, not inside this function
        var currentNode = this.firstNode;
        var item = currentNode.item;
        currentNode = currentNode.nextNode;
        return item;
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

    let sll = new stacklinkedlist();

    inputs[0].forEach(function (item) {
        if (item == 777) {
            console.log("Popped from stack: " + sll.pop());
            console.log("Stack size: " + sll.size());
        } else {
            sll.push(item);
            console.log("Pushed on: " + item);
            console.log("Stack size: " + sll.size());
        }
    });
        
    let finalSize = sll.size();
    if (finalSize > 0) {
        console.log("Final stack (last-first/top-bottom/newest-oldest):");
        console.log(sll.stackValues());
    } else if (sll.isEmpty()) {
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