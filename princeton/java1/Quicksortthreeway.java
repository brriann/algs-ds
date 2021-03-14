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

public class Quicksortthreeway {

    private static Random random;
    private static long seed; 

    static {
        // this is how the seed was set in Java 1.4
        seed = System.currentTimeMillis();
        random = new Random(seed);
    }

    public static boolean onUbuntu = true;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/dev" 
        : "/Users/brianfoster/dev";

    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/12shellsort1.txt";



    public Quicksortthreeway() {

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

    private static int compareToInt(int a, int b) {
        if (a < b) {
            return -1;
        } else if (a > b) {
            return 1;
        } else {
            return 0;
        }
    }

    private void sort(int[] a) {
        shuffle(a);
        sort(a, 0, a.length - 1);
    }

    private void sort(int[] a, int lo, int hi) {
        if (hi <= lo) {
            return;
        }

        int lt = lo, gt = hi;
        int v = a[lo];
        int i = lo;

        while (i <= gt) {
            int cmp = compareToInt(a[i], v);
            if (cmp < 0) {
                exchange(a, lt++, i++);
            } else if (cmp > 0) {
                exchange(a, i, gt--);
            } else {
                i++;
            }
        }

        sort(a, lo, lt - 1);
        sort(a, gt + 1, hi);
    }

    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        System.out.println("Unsorted list:");
        System.out.println(Arrays.toString(list));

        Quicksortthreeway qs = new Quicksortthreeway();
        qs.sort(list);

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