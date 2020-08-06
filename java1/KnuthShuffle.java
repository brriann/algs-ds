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

public class KnuthShuffle {

    private static Random random;
    private static long seed;

    public static boolean onUbuntu = false;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/Dev" 
        : "/Users/brianfoster/dev";

    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/13shuffle2.txt";

     public KnuthShuffle() {

         seed = System.currentTimeMillis();
         random = new Random(seed);
     }

     private static void exchange(int[] array, int i, int j) {
         int swap = array[i];
         array[i] = array[j];
         array[j] = swap;
     }


    public static void shuffle(int[] list) {
        int N = list.length;

        for (int i = 0; i < N; i++) {
            int r = random.nextInt(i + 1);
            exchange(list, i, r);
        }
    }
    
    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        System.out.println("Sorted list:");
        System.out.println(Arrays.toString(list));

        KnuthShuffle ks = new KnuthShuffle();
        ks.shuffle(list);

        System.out.println("Shuffled list:");
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