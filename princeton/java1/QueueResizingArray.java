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

public class QueueResizingArray {

    public static boolean onUbuntu = true;

    public static String baseDevFolder = onUbuntu 
        ? "/home/ubuntu/Dev" 
        : "/Users/brianfoster/dev";
        
    public static String INPUT_FILE_PATH = baseDevFolder + "/algs-ds/input/9stack2.txt";

    private int[] queueArray;
    private int N = 0;
    private int first = 0;
    private int last = 0;

    public QueueResizingArray() {
        queueArray = new int[1];
    }

    public void enQueue(int item) {
        if (N == queueArray.length) {
            resize(2 * queueArray.length);
        }
        queueArray[last++] = item;
        if (last == queueArray.length) {
            last = 0;
        }
        N++;
    }

    public int deQueue() {
        int item = queueArray[first];
        queueArray[first] = -1; // using primitive int's instead of Integer.... -1 will be 'null' value
        N--;
        first++;
        if (first == queueArray.length) {
            first = 0;
        }
        if (N > 0 && N == queueArray.length / 4) {
            resize(queueArray.length / 2);
        }
        return item;
    }

    private void resize(int capacity) {
        if (capacity >= N) {
            int[] copyArray = new int[capacity];
            for (int i = 0; i < N; i++) {
                copyArray[i] = queueArray[(first + i) % queueArray.length];
            }
            queueArray = copyArray;
            first = 0;
            last = N;
        }
        
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public int size() {
        return N;
    }

    public int[] queueValues() {
        if (isEmpty() || size() == 0) {
            return new int[0];
        } else {
            int[] queueValues = new int[size()];
            for (int i = 0; i < N; i++) {
                queueValues[i] = queueArray[(first + i) % queueArray.length];
            }
            return queueValues;
        }
    }

    public boolean hasNext() {
        int i = N;
        return i > 0;
    }

    public int next() {
        // for a true iterator, this would be assigned outside of the next method.
        int i = N;
        return queueArray[--i];
    }

    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {

        QueueResizingArray qra = new QueueResizingArray();

        for (int i : inputs[0]) {
            if (i == 777) {
                System.out.println(String.format("dequeued from queue: %d", qra.deQueue()));
                System.out.println(String.format("Queue size: %d", qra.size()));
            } else {
                qra.enQueue(i);
                System.out.println(String.format("Enqueued: %d", i));
                System.out.println(String.format("Queue size: %d", qra.size()));
            }
        }
        int finalSize = qra.size();
        if (finalSize > 0) {
            System.out.println("Final queue (first-last/oldest-newest):");
            System.out.println(Arrays.toString(qra.queueValues()));
        } else if (qra.isEmpty()) {
            System.out.println("Final queue is empty.");
        } else {
            System.out.println("Error? final size and isEmpty don't agree.");
        }
    }
    
    public static void main(String[] args) {
        if (args.length > 0) {
            runClient(CliReader.readArgTo2DArray(args[0]));
        } else {
            runClient(FileReader.readLinesTo2DArray(INPUT_FILE_PATH));
        }
    }
}