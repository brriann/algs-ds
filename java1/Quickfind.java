// CLI usage: 
// java Quickfind n/p-q/p-q/p-q/p-q
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

package java1;

public class Quickfind {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/1unionfind1.txt";
    
    private int N;

    public Quickfind() {

    }

    public Quickfind(int n) {
        N = n;
    }
    
    public void union(int p, int q) {
        // This file only implements the UF client.
    }

    public boolean connected(int p, int q) {
        return true;
    }

    public int find(int p) {
        // This file only implements the UF client.
        return 5;
    }

    public int count() {
        // This file only implements the UF client.
        return 10;
    }

    private static void runClient(int[][] inputs) {
        int n = inputs[0][0];
        Quickfind uf = new Quickfind(n);

        for (int i = 1; i < inputs.length; i++) {
            int p = inputs[i][0];
            int q = inputs[i][1];

            if (!uf.connected(p, q)) {
                uf.union(p, q);
                System.out.println(String.format("%d <---> %d", p, q));
            } else {
                System.out.println(String.format("(%d and %d are connected.)", p, q));
            }
        }
    }

    //
    // CLIENT
    //
    
    public static void main(String[] args) {
        if (args.length > 0) {
            runClient(CliReader.readArgTo2DArray(args[0]));
        } else {
            runClient(FileReader.readLinesTo2DArray(INPUT_FILE_PATH));
        }
    }
}