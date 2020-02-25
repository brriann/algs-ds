// CLI usage: 
// node 3quickunion.js n/p-q/p-q/p-q/p-q
//
// File usage:
// n
// p q
// p q
// p q

//
// Lazy approach of Union-Find
// Read an array size "n"
// Read rows of elt's "p" and "q"
//
// integer array id[] of size n.
// id[i] is parent of i
// root of i is id[id[id[...id[i]...]]]
// p and q are connected iff they have the same root
//
// Find: check if p and q have the same root
// Union: to merge components containing p and q,
//     set the id of p's root to the id of q's root
//
// Trees get too tall
// Find too expensive (could be N array accesses)

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
        let i = this.root(p);
        let j = this.root(q);
        
        this.ids[i] = this.ids[j];
        
        console.log(p + " <---> " + q);
        console.log(this.ids);
    }

    connected(p, q) {
        return this.root(p) === this.root(q);
    }

    root(i) {
        while (i !== this.ids[i]) {
            i = this.ids[i];
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