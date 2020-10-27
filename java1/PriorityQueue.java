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

public class PriorityQueue {

    public static boolean onUbuntu = true;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/dev" 
        : "/Users/brianfoster/dev";

    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/14priorityqueue.txt";

    private int[] pq;
    private int N;
    private int Capacity;


    public PriorityQueue() {

    }

    public PriorityQueue(int capacity) {
        pq = new int[capacity + 1];
        Capacity = capacity;
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public boolean isOverCapacity() {
        return N > Capacity;
    }

    public void insert(int x) {
        pq[N++] = x;
    }

    public int deleteMax() {
        int max = 0;
        for (int i = 1; i < N; i++) {
            if (less(pq[max], pq[i])) {
                max = i;
            }
        }
        exchange(pq, max, N - 1);
        return pq[--N];
    }

    public int[] getArray() {
        int[] copyOfCapacity = new int[Capacity];
        for (int i = 0; i < Capacity; i ++) {
            copyOfCapacity[i] = pq[i];
        }
        return copyOfCapacity;
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

    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        // Find minimum 5 values in stream

        PriorityQueue pq = new PriorityQueue(7);

        for (int i = 0; i < list.length; i++) {
            pq.insert(list[i]);
            print(String.format("Inserted: %d", list[i]));

            if (pq.isOverCapacity()) {
                int deletedMax = pq.deleteMax();
                print(String.format("Deleted Max: %d", deletedMax));
            }
        }
        print(Arrays.toString(pq.getArray()));


    }

    private static void print(String output) {
        System.out.println(output);
    }
    
    public static void main(String[] args) {
        if (args.length > 0) {
            runClient(CliReader.readArgTo2DArray(args[0]));
        } else {
            runClient(FileReader.readLinesTo2DArray(INPUT_FILE_PATH));
        }
    }
}