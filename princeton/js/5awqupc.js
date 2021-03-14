// CLI usage: 
// node 4wqu.js n/p-q/p-q/p-q/p-q
//
// File usage:
// n
// p q
// p q
// p q

//
// Weighted Quick Union
// Read an array size "n"
// Read rows of elt's "p" and "q"
//
// integer array id[] of size n.
// integer array size[] of size n
// size[i] tracks the size of object whose root is id[i]
// id[i] is parent of i
// root of i is id[id[id[...id[i]...]]]
// p and q are connected iff they have the same root
//
// Find: check if p and q have the same root
// Union: to merge components containing p and q,
//     set the id of smaller tree's root to the id of larger tree's root
//     and update the size[] array
//
// 2-pass Path Compression: add 2nd loop to root(), to set id[] of each examined node to the root
//
// By adding smaller trees to larger trees, Tree height grows slower (and is limited to at most lgN)

var file = require('/home/ubuntu/Dev/algs-ds/tools/file.js');
var cli = require('/home/ubuntu/Dev/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/1unionfind1.txt'

class unionfind { 

    constructor(n) {
        this.n = n;
        this.ids = [];
        this.size = [];
        for (let i = 0; i < n; i++) {
            this.ids.push(i);
            this.size.push(1);
        }
    }

    union(p, q) {
        console.log("UNION " + p + " and " + q);
        let i = this.root(p);
        let j = this.root(q);

        if (i === j) {
            console.log("(" + p + " connects to " + q + ")");
            return;
        }

        if (this.size[i] < this.size[j]) {
            this.ids[i] = j;
            this.size[j] += this.size[i];
        } else {
            this.ids[j] = i;
            this.size[i] += this.size[j];
        }
        
        console.log(p + " <---> " + q);
        console.log(this.ids);
        console.log(this.size);
    }

    connected(p, q) {
        console.log("CONNECTED " + p + " and " + q);
        return this.root(p) === this.root(q);
    }

    root(i) {
        console.log("ROOT " + i);
        var nodesToSet = [];
        var nodesThatWereSet = 0;
        var originalChild = i;

        while (i !== this.ids[i]) {
            nodesToSet.push(i);
            i = this.ids[i];
        }

        if (nodesToSet.length > 0) {
            console.log('examining ' + originalChild + ', set nodes to root ' + i + ': ');
            console.log(nodesToSet);
        }

        // 2nd pass to set examined nodes to root
        for (let j in nodesToSet) {
            if (this.ids[j] !== i) {
                this.ids[j] = i;
                this.size[i] += this.size[j];
                nodesThatWereSet++;
            }
        }

        if (nodesToSet.length > 0 && nodesThatWereSet > 0) {
            console.log('(' + nodesThatWereSet + ' examined nodes set.)');
            console.log(this.ids);
            console.log(this.size);
        }

        return i;
    }
}

function runClient (inputs) {
    let n = inputs[0][0];
    let uf = new unionfind(n);

    for (let i = 1; i < inputs.length; i++) {
        var p = inputs[i][0];
        var q = inputs[i][1];

        if (!uf.connected(p, q)) { 
            uf.union(p, q);
        } else {
            console.log("(" + p + " and " + q + " are connected.)");
        }
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