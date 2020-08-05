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

public class Shellsort {

    public static boolean onUbuntu = false;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/Dev" 
        : "/Users/brianfoster/dev";

    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/12shellsort1.txt";

     public Shellsort() {

     }

     private static boolean less(int v, int w) {
         // this would be more meaningful for Comparables.
         // but only doing int's for now.
         return v < w;
     }

     private static void exchange(int[] array, int i, int j) {
         int swap = array[i];
         array[i] = array[j];
         array[j] = swap;
     }


    public static void sort(int[] list) {
        int N = list.length;

        int h = 1;

        while (h < N / 3) {
            h = 3 * h + 1;
        }

        while (h >= 1) {
            System.out.println(String.format("H is %d", h));

            for (int i = h; i < N; i++) {
                for (int j = i; j >= h && less(list[j], list[j-h]); j -= h) {
                    System.out.println(String.format("i is %d, j is %d", i, j));
                    exchange(list, j, j - h);
                }
            }
            h = h / 3;
        }
    }
    
    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        System.out.println("Unsorted list:");
        System.out.println(Arrays.toString(list));

        Shellsort ss = new Shellsort();
        ss.sort(list);

        System.out.println("Sorted list:");
        System.out.println(Arrays.toString(list));
    }
    
    public static void main(String[] args) {
        if (args.length > 0) {
            runClient(CliReader.readArgTo2DArray(args[0]));
        } else {
            runClient(FileReader.readLinesTo2DArray(INPUT_FILE_PATH));
        }
    }
}