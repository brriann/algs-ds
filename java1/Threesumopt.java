// CLI usage: 
// node 8threesumopt.js 4 -4 2 6 0 -2 8 10 -6 ( WILL NOT USE CLI)
//
// File usage:
//4 -4 2 6 0 -2 8 10 -6

//
// Optimized implementation of three-sum
// Read an array of ints - Identify all triples that sum to zero
// Sort the list
// for each pair of numbers a[i] and a[j], binary search for -(a[i] + a[j])
//

package java1;

import java.util.Arrays;

public class Threesumopt {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/8threesum1.txt";

    public Threesumopt() {

    }

    public void threesum(int[] list) {
        int n = list.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int ij = list[i] + list[j];
            }
        }
        System.out.println(String.format("count: %d", count));
    }

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        Threesumopt tso = new Threesumopt();
        tso.threesum(list);
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