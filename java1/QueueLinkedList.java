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

public class QueueLinkedList {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/9stack2.txt";
    
    private Node firstNode = null;
    private Node lastNode = null;

    private class Node {
        int item;
        Node nextNode;
    }
    
    public QueueLinkedList() {

    }

    public void enQueue(int item) {
        Node oldLastNode = lastNode;
        lastNode = new Node();
        lastNode.item = item;
        lastNode.nextNode = null;
        if (isEmpty()) {
            firstNode = lastNode;
        } else  {
            oldLastNode.nextNode = lastNode;
        }
    }

    public int deQueue() {
        int item = firstNode.item;
        firstNode = firstNode.nextNode;
        if (isEmpty()) {
            lastNode = null;
        }
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

    public int[] queueValues() {
        if (isEmpty() || size() == 0) {
            return new int[0];
        } else {
            int[] queueValues = new int[size()];
            int index = 0;
            Node nodeTracker = firstNode;

            while (nodeTracker != null) {
                queueValues[index++] = nodeTracker.item;
                nodeTracker = nodeTracker.nextNode;
            }
            return queueValues;
        }
    }

    //
    // CLIENT
    //

    private static void runClient(int[][] inputs) {

        QueueLinkedList qll = new QueueLinkedList();

        for (int i : inputs[0]) {
            if (i == 777) {
                System.out.println(String.format("dequeued from queue: %d", qll.deQueue()));
                System.out.println(String.format("Queue size: %d", qll.size()));
            } else {
                qll.enQueue(i);
                System.out.println(String.format("Enqueued: %d", i));
                System.out.println(String.format("Queue size: %d", qll.size()));
            }
        }
        int finalSize = qll.size();
        if (finalSize > 0) {
            System.out.println("Final queue (first-last/oldest-newest):");
            System.out.println(Arrays.toString(qll.queueValues()));
        } else if (qll.isEmpty()) {
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