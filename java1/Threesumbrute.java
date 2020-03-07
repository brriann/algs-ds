// CLI usage: 
// java Insertionsort 1-3-5-7-9-12-14-15-17-18-19-22-25-27-29-35-36-38-45-47-49-51-55-57-59-62-64-65-67-68-69
//
// File usage:
// 1 3 5 7 9 12 14 15 17 18 19 22 25 27 29 35 36 38 45 47 49 51 55 57 59 62 64 65 67 68 69

//
// Simple client for Insertion Sort to be used in Threesum
// Read an array of ints
// Sort using Insertion Sort
// Return sorted list
//

package java1;

import java.util.Arrays;

public class Threesumbrute {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/8threesum1.txt";

    public Threesumbrute() {

    }

    public void threesum(int[] list) {
        int n = list.length;
        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (list[i] + list[j] + list[k] == 0) {
                        System.out.println(String.format("3-SUM: %d %d %d", list[i], list[j], list[k]));
                        count++;
                    }
                }
            }
        }
        System.out.println(String.format("count: %d", count));
    }

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        Threesumbrute tsb = new Threesumbrute();
        tsb.threesum(list);
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