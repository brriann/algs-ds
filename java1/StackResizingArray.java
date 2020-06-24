// CLI usage: 
// java StackLinkedList 1-2-3-777-4-5-6-777-777-777
//
// File usage:
// 1 2 3 777 4 5 6 777 777 777

//
// Stack of ints implemented by linked list
// ints in input stream will be pushed onto stack
// input of 777 will print popped int from stack
//

package java1;

import java.util.Arrays;

public class StackResizingArray {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/9stack2.txt";
    public static String INPUT_FILE_PATH_2 = "/Users/brianfoster/dev/algs-ds/input/9stack2.txt";
    
    private int[] stackArray;
    private int N = 0;
    
    public StackResizingArray() {
        stackArray = new int[1];
    }

    public void push(int item) {
        // if array is full, double its size.
        if (N == stackArray.length) {
            resize(2 * stackArray.length);
        }
        stackArray[N++] = item;
    }

    public int pop() {
        // if array is 1/4 full, halve its size
        if (N > 0 && N == (stackArray.length / 4)) {
            resize(stackArray.length / 2);
        }
        return stackArray[--N];
    }

    private void resize(int capacity) {
        int[] copyArray = new int[capacity];
        for (int i = 0; i < N; i++) {
            copyArray[i] = stackArray[i];
        }
        stackArray = copyArray;
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public int size() {
        return N;
    }

    public int[] stackValues() {
        if (isEmpty() || size() == 0) {
            return new int[0];
        } else {
            int[] stackValues = new int[size()];
            for (int i = 0; i < N; i++) {
                stackValues[i] = stackArray[i];
            }
            return stackValues;
        }
    }

    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {

        StackResizingArray sra = new StackResizingArray();

        for (int i : inputs[0]) {
            if (i == 777) {
                System.out.println(String.format("Popped from stack: %d", sra.pop()));
                System.out.println(String.format("Stack size: %d", sra.size()));
            } else {
                sra.push(i);
                System.out.println(String.format("Pushed on: %d", i));
                System.out.println(String.format("Stack size: %d", sra.size()));
            }
        }
        int finalSize = sra.size();
        if (finalSize > 0) {
            System.out.println("Final stack (last-first/top-bottom/newest-oldest):");
            System.out.println(Arrays.toString(sra.stackValues()));
        } else if (sra.isEmpty()) {
            System.out.println("Final stack is empty.");
        } else {
            System.out.println("Error? final size and isEmpty don't agree.");
        }
    }
    
    public static void main(String[] args) {
        if (args.length > 0) {
            runClient(CliReader.readArgTo2DArray(args[0]));
        } else {
            runClient(FileReader.readLinesTo2DArray(INPUT_FILE_PATH_2));
        }
    }
}