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

public class Insertionsort2 {

    public static boolean onUbuntu = false;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/Dev" 
        : "/Users/brianfoster/dev";

    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/7insertionsort1.txt";

     public Insertionsort2() {

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


    public static void newSort(int[] list) {
        for (int i = 0; i < list.length; i++) {
            for (int j = i; j > 0; j--) {
                if (less(list[j], list[j - 1])) {
                    exchange(list, j, j - 1);
                } else {
                    break;
                }
            }
        }
    }

    // from a previous implementation of Insertionsort...see Insertionsort.java
    public static void oldSort(int[] list) {
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
    
    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        System.out.println("Unsorted list:");
        System.out.println(Arrays.toString(list));

        Insertionsort2 is = new Insertionsort2();
        is.newSort(list);

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