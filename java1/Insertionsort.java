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

public class Insertionsort {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/7insertionsort1.txt";

    public Insertionsort() {

    }

    public void sort(int[] list) {
        for (int i = 1; i < list.length; i++) {
            int j = i - 1;
            int temp = list[i];
            while (j >= 0 && list[j] > temp) {
                list[j + 1] = list[j];
                j -= 1;
            }
            list[j + 1] = temp;
        }
    }

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        System.out.println("Unsorted list:");
        System.out.println(Arrays.toString(list));

        Insertionsort is = new Insertionsort();
        is.sort(list);

        System.out.println("Sorted list:");
        System.out.println(Arrays.toString(list));
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