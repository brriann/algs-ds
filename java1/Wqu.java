// CLI usage: 
// java Wqu n/p-q/p-q/p-q/p-q
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
// By adding smaller trees to larger trees, Tree height grows slower (and is limited to at most lgN)

package java1;
import java.util.Arrays;

public class Wqu {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/1unionfind1.txt";
    
    private int N;
    private int[] ids;

    public Wqu() {

    }

    public Wqu(int n) {
        N = n;
        ids = new int[N];
        for (int i = 0; i < N; i++) {
            ids[i] = i;
        }
    }
    
    public void union(int p, int q) {
        int i = root(p);
        int j = root(q);
        ids[i] = ids[j];
        System.out.println(String.format("%d <---> %d", p, q));
        System.out.println(Arrays.toString(ids));
    }

    public boolean connected(int p, int q) {
        return root(p) == root(q);
    }

    private int root(int i) {
        while (i != ids[i]) {
            i = ids[i];
        }
        return i;
    }

    private static void runClient(int[][] inputs) {
        int n = inputs[0][0];
        Wqu uf = new Wqu(n);

        for (int i = 1; i < inputs.length; i++) {
            int p = inputs[i][0];
            int q = inputs[i][1];

            if (!uf.connected(p, q)) {
                uf.union(p, q);
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