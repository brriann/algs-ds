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

public class Heapsort {

    public static boolean onUbuntu = false;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/dev" 
        : "/Users/brianfoster/dev";

    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/14priorityqueue.txt";

    private int[] hsa;
    private int Capacity;
    private int NN;

    public Heapsort(int[] list) {
        hsa = new int[list.length + 1];
        Capacity = list.length + 1;

        for (int i = 0; i < list.length; i++) {
            insert(list[i]);
        }
    }

    public void insert(int x) {
        hsa[++NN] = x;
        swim(NN);
    }

    private void swim(int k) {
        while (k > 1 && less(hsa, k / 2, k)) {
            exchange(hsa, k, k / 2);
            k = k / 2;
        }
    }

    public int[] getArray() {
        int[] copyOfCapacity = new int[Capacity];
        for (int i = 0; i < Capacity; i ++) {
            copyOfCapacity[i] = hsa[i];
        }
        return copyOfCapacity;
    }

    public Heapsort() {

    }

    public void sort() {
        int N = hsa.length;

        for (int k = N / 2; k >= 1; k--) {
            sink(hsa, k, N);
        }

        while (N > 1) {
            exchange(hsa, 1, N);
            sink(hsa, 1, --N);
        }
    }

    private void sink(int[] a, int k, int N) {
        while (2 * k <= N) {
            int j = 2 * k;
            if (j < N && less(a, j, j + 1)) {
                j++;
            }
            if (!less(a, k, j)) {
                break;
            }
            exchange(a, k, j);
            k = j;
        }
    }

    private boolean less(int[] a, int v, int w) {
        // this would be more meaningful for Comparables.
        // but only doing int's for now.
        return a[v - 1] < a[w - 1];
    }

    private static void exchange(int[] array, int i, int j) {
        int swap = array[i - 1];
        array[i - 1] = array[j - 1];
        array[j - 1] = swap;
    }

    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {
        int[] list = inputs[0];

        // Find minimum 5 values in stream

        Heapsort hs = new Heapsort(list);

        hs.sort();

        print("Unsorted list:");
        print(Arrays.toString(list));

        print("Heap-sorted list:");
        print(Arrays.toString(hs.getArray()));


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