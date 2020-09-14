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

public class BinaryHeap {

    public static boolean onUbuntu = false;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/dev" 
        : "/Users/brianfoster/dev";

    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/14priorityqueue.txt";

    private int[] pq;
    private int N;
    private int Capacity;


    public BinaryHeap() {

    }

    public BinaryHeap(int capacity) {
        pq = new int[capacity + 2];
        Capacity = capacity;
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public boolean isOverCapacity() {
        return N > Capacity;
    }

    public void insert(int x) {
        pq[++N] = x;
        swim(N);
    }

    public int deleteMax() {
        int max = pq[1];
        exchange(pq, 1, N--);
        sink(1);
        //pq[N + 1] = null;
        return max;
    }

    public int[] getArray() {
        int[] copyOfFive = new int[6];
        for (int i = 0; i < 6; i ++) {
            copyOfFive[i] = pq[i];
        }
        return copyOfFive;
    }

    private void swim(int k) {
        while (k > 1 && less(k / 2, k)) {
            exchange(pq, k, k / 2);
            k = k / 2;
        }
    }

    private void sink(int k) {
        while (2 * k <= N) {
            int j = 2 * k;
            if (j < N && less(j, j + 1)) {
                j++;
            }
            if (!less(k, j)) {
                break;
            }
            exchange(pq, k, j);
            k = j;
        }
    }

    private boolean less(int v, int w) {
        // this would be more meaningful for Comparables.
        // but only doing int's for now.
        return pq[v] < pq[w];
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

        BinaryHeap pq = new BinaryHeap(5);

        for (int i = 0; i < list.length; i++) {
            if (pq.isOverCapacity()) {
                int deletedMax = pq.deleteMax();
                print(String.format("Deleted Max: %d", deletedMax));
            } else {
                pq.insert(list[i]);
            print(String.format("Inserted: %d", list[i]));
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