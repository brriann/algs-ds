// CLI usage: 
// node 2quickfind.js n/p-q/p-q/p-q/p-q
//
// File usage:
// n
// p q
// p q
// p q

//
// Eager approach of Union-Find
// Read an array size "n"
// Read rows of elt's "p" and "q"
//
// integer array id[] of size n.
// p and q are connected iff they have the same id
//
// Find: check if p and q have the same id
// Union: to merge components containing p and q,
//     change all entries whose id equals id[p] to id[q]
//
// Trees are flat, but too expensive to keep them flat.
// Union too expensive (N array accesses)

var file = require('/home/ubuntu/Dev/algs-ds/tools/file.js');
var cli = require('/home/ubuntu/Dev/algs-ds/tools/cli.js');

const INPUT_FILE_PATH = '/home/ubuntu/Dev/algs-ds/input/1unionfind1.txt'

class unionfind {

    constructor(n) {
        this.n = n;
        this.ids = [];
        for (let i = 0; i < n; i++) {
            this.ids.push(i);
        }
    }

    union(p, q) {
        let pid = this.ids[p];
        let qid = this.ids[q];
        for (let i = 0; i < this.n; i++) {
            if (this.ids[i] === pid) {
                this.ids[i] = qid;
            }
        }
        console.log(p + " <---> " + q);
        console.log(this.ids);
    }

    connected(p, q) {
        return this.ids[p] === this.ids[q];
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