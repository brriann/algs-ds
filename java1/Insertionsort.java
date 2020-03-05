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

public class Insertionsort {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/7insertionsort1.txt";

    public Insertionsort() {

    }

    public int[] sort(int[] unsortedList) {
        return unsortedList;
    }

    private static void runClient(int[][] inputs) {
        int[] unsortedList = inputs[0];

        Insertionsort is = new Insertionsort();

        int[] sortedList = is.sort(unsortedList);

        System.out.println("Unsorted list:");
        System.out.println(unsortedList);

        System.out.println("Sorted list:");
        System.out.println(sortedList);
    }

    //
    // CLIENT
    //
    
    public static void main(String[] args) {
        if (args.length > 0) {
            runClient(CliReader.readArgTo2DArray(args[0]));
        } else {
            runClient(FileReader.readLinesTo2DArray(INPUT_FILE_PATH));
        }
    }
}