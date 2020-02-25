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
import java.util.Arrays;

public class Quickfind {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/1unionfind1.txt";
    
    private int N;
    private int[] ids;

    public Quickfind() {

    }

    public Quickfind(int n) {
        N = n;
        ids = new int[N];
        for (int i = 0; i < N; i++) {
            ids[i] = i;
        }
    }
    
    public void union(int p, int q) {
        int pid = ids[p];
        int qid = ids[q];
        for (int i = 0; i < N; i++) {
            if (ids[i] == pid) {
                ids[i] = qid;
            }
        }
        System.out.println(String.format("%d <---> %d", p, q));
        System.out.println(Arrays.toString(ids));
    }

    public boolean connected(int p, int q) {
        return ids[p] == ids[q];
    }

    private static void runClient(int[][] inputs) {
        int n = inputs[0][0];
        Quickfind uf = new Quickfind(n);

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