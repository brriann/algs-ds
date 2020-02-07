const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output:process.stdout
});

rl.question("Enter n: ", function(n) {
    rl.question("Enter p: ", function(p) {
        rl.question("Enter q: ", function(q) {
            var uf = new unionfind(n);
            if (!uf.connected(p, q)) { 
                uf.union(p, q);
                console.log(p + " " + q);
            }
            rl.close();
        });
    });
});

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


