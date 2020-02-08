// compile this script with "javac Unionfind.java"
// invoke this script with an int array from CLI as "java Unionfind"

// this defines a basic "dynamic connectivity" client for Union Find implementations

import java.util.*;

public class Unionfind {

    private int N;

    private int P;
    private int Q;

    public Unionfind() {

    }

    public Unionfind(int n) {
        N = n;
    }

    public void setN(int n) {
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
        
        Unionfind uf = new Unionfind();
        int[] input = uf.takeCommandLineInput();
        // int[] input = uf.takeFileInput();
    
        uf.setN(input[0]);

        int p = input[1];
        int q = input[2];
        

        if (!uf.connected(p, q)) {
            uf.union(p, q);
            System.out.println(p + " " + q);
        }

        
    }

    public int[] takeCommandLineInput() {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter n: ");
        int n = scan.nextInt();
        System.out.println("Enter p: ");
        int p = scan.nextInt();
        System.out.println("Enter q: ");
        int q = scan.nextInt();
        scan.close();
        int[] npq = new int[3];
        npq[0] = n;
        npq[1] = p;
        npq[2] = q;
        return npq;
    }

    public int[] takeFileInput() {
        return new int[3];
    }
}