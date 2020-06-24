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

public class StackLinkedList {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/9stack1.txt";
    public static String INPUT_FILE_PATH_2 = "/Users/brianfoster/dev/algs-ds/input/9stack2.txt";
    
    private Node firstNode = null;

    private class Node {
        int item;
        Node nextNode;
    }
    
    public StackLinkedList() {

    }

    public void push(int item) {
        Node oldFirstNode = firstNode;
        firstNode = new Node();
        firstNode.item = item;
        firstNode.nextNode = oldFirstNode;
    }

    public int pop() {
        int item = firstNode.item;
        firstNode = firstNode.nextNode;
        return item;
    }

    public boolean isEmpty() {
        return firstNode == null;
    }

    public int size() {
        int sizeTracker = 0;

        Node nodeTracker = firstNode;
        while (nodeTracker != null) {
            sizeTracker++;
            nodeTracker = nodeTracker.nextNode;
        }
        return sizeTracker;
    }

    public int[] stackValues() {
        if (isEmpty() || size() == 0) {
            return new int[0];
        } else {
            int[] stackValues = new int[size()];
            int index = 0;
            Node nodeTracker = firstNode;

            while (nodeTracker != null) {
                stackValues[index++] = nodeTracker.item;
                nodeTracker = nodeTracker.nextNode;
            }
            return stackValues;
        }
    }

    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {

        StackLinkedList sll = new StackLinkedList();

        for (int i : inputs[0]) {
            if (i == 777) {
                System.out.println(String.format("Popped from stack: %d", sll.pop()));
                System.out.println(String.format("Stack size: %d", sll.size()));
            } else {
                sll.push(i);
                System.out.println(String.format("Pushed on: %d", i));
                System.out.println(String.format("Stack size: %d", sll.size()));
            }
        }
        int finalSize = sll.size();
        if (finalSize > 0) {
            System.out.println("Final stack (last-first/top-bottom/newest-oldest):");
            System.out.println(Arrays.toString(sll.stackValues()));
        } else if (sll.isEmpty()) {
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