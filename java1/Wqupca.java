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
// 2-pass Path Compression: add 2nd loop to root(), to set id[] of each examined node to the root
//
// By adding smaller trees to larger trees, Tree height grows slower (and is limited to at most lgN)

package java1;
import java.util.Arrays;
import java.util.ArrayList;

public class Wqupca {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/1unionfind1.txt";
    
    private int N;
    private int[] ids;
    private int[] size;

    public Wqupca() {

    }

    public Wqupca(int n) {
        N = n;
        ids = new int[N];
        size = new int[N];

        for (int i = 0; i < N; i++) {
            ids[i] = i;
            size[i] = 1;
        }
    }
    
    public void union(int p, int q) {
        System.out.println(String.format("UNION %d and %d", p, q));
        int i = root(p);
        int j = root(q);

        if (i == j) {
            System.out.println(String.format("(%d connects to %d)", p, q));
            return;
        }

        if (size[i] < size[j]) {
            ids[i] = j;
            size[j] += size[i];
        } else {
            ids[j] = i;
            size[i] += size[j];
        }


        System.out.println(String.format("%d <---> %d", p, q));
        System.out.println(Arrays.toString(ids));
        System.out.println(Arrays.toString(size));
    }

    public boolean connected(int p, int q) {
        System.out.println(String.format("CONNECTED %d and %d", p, q));
        return root(p) == root(q);
    }

    private int root(int i) {
        System.out.println(String.format("ROOT %d", i));
        ArrayList<Integer> nodesToSet = new ArrayList<Integer>();
        int nodesThatWereSet = 0;
        int originalChild = i;


        while (i != ids[i]) {
            nodesToSet.add(i);
            i = ids[i];
        }

        if (nodesToSet.size() > 0) {
            System.out.println(String.format("examining %d, set nodes to root %d", originalChild, i));
            System.out.println(Arrays.toString(nodesToSet.toArray()));
        }

        // 2nd pass to set examined nodes to root
        for (Integer j : nodesToSet) {
            if (ids[j] != i) {
                ids[j] = i;
                size[i] += size[j];
                nodesThatWereSet++;
            }
        }

        if (nodesToSet.size() > 0 && nodesThatWereSet > 0) {
            System.out.println(String.format("(%d examined nodes set.)", nodesThatWereSet));
            System.out.println(Arrays.toString(ids));
            System.out.println(Arrays.toString(size));
        }

        return i;
    }

    private static void runClient(int[][] inputs) {
        int n = inputs[0][0];
        Wqupca uf = new Wqupca(n);

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