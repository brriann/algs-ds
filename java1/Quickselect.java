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
import java.util.Random;

public class Quickselect {

    private static Random random;
    private static long seed; 

    static {
        // this is how the seed was set in Java 1.4
        seed = System.currentTimeMillis();
        random = new Random(seed);
    }

    public static boolean onUbuntu = false;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/Dev" 
        : "/Users/brianfoster/dev";

    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/12shellsort1.txt";



    public Quickselect() {

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


    public static int uniform(int n) {
        if (n <= 0) throw new IllegalArgumentException("argument must be positive: " + n);
        return random.nextInt(n);
    }

    public static void shuffle(int[] a) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            int r = i + uniform(n-i);     // between i and n-1
            int temp = a[i];
            a[i] = a[r];
            a[r] = temp;
        }
    }

    private static int partition(int[] a, int lo, int hi) {
        int i = lo, j = hi + 1;

        while (true) {
            while (less(a[++i], a[lo])) {
                if (i == hi) break;
            }
            while (less(a[lo], a[--j])) {
                if (j == lo) break;
            }
            if (i >= j) break;
            exchange(a, i, j);
        }

        exchange(a, lo, j);
        return j;
    }

    public static int select(int[] a, int k) {
        shuffle(a);
        int lo = 0, hi = a.length - 1;
        while (hi > lo) {
            int j = partition(a, lo, hi);
            if (j < k) {
                lo = j + 1;
            } else if (j > k) {
                hi = j - 1;
            } else {
                return a[k];
            }
        }
        return a[k];
    }

    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        System.out.println("Unsorted list:");
        System.out.println(Arrays.toString(list));

        Quickselect qs = new Quickselect();
        int kth = qs.select(list, 25);

        System.out.println("25th smallest item::");
        System.out.println(kth);
    }
    
    public static void main(String[] args) {
        if (args.length > 0) {
            runClient(CliReader.readArgTo2DArray(args[0]));
        } else {
            runClient(FileReader.readLinesTo2DArray(INPUT_FILE_PATH));
        }
    }
}