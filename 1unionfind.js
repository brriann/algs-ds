
function takeCommandLineInput() {
    const readline = require("readline");
    const rl = readline.createInterface({
        input: process.stdin,
        output:process.stdout
    });

    rl.question("Enter n: ", function(n) {
        rl.question("Enter p: ", function(p) {
            rl.question("Enter q: ", function(q) {
                rl.close();
                return [n, p, q];
            });
        });
    });
}

function TakeFileInput() {
    return [10, 5, 5];
}

class unionfind { 
    constructor(n) {
        this.n = n;
    }
    union(p, q) {
        // TODO: implement union
    }

    connected(p, q) {
        return p === q;
    }

    find(p) {

    }

    count() {

    }
}

//
// Program starts here.
//

var npq = takeCommandLineInput();

var uf = new unionfind(npq[0]);
var p = npq[1];
var q = npq[2];

if (!uf.connected(p, q)) { 
    uf.union(p, q);
    console.log(p + " " + q);
}


