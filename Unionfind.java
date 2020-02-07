// compile this script with "javac Unionfind.java"
// invoke this script with an int array from CLI as "java Unionfind"

// this defines a basic "dynamic connectivity" client for Union Find implementations

import java.util.*;

public class Unionfind {

    private int N;

    private int P;
    private int Q;

    public Unionfind(int n) {
        N = n;
    }

    public void union(int p, int q) {
        // TODO: implement union
    }

    public boolean connected(int p, int q) {
        return p == q;
    }

    public int find(int p) {
        return P;
    }

    public int count() {
        return P + Q;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter n: ");
        int n = scan.nextInt();

        Unionfind uf = new Unionfind(n);

        System.out.println("Enter p: ");
        int p = scan.nextInt();
        System.out.println("Enter q: ");
        int q = scan.nextInt();

        if (!uf.connected(p, q)) {
            uf.union(p, q);
            System.out.println(p + " " + q);
        }

        scan.close();
    }
}