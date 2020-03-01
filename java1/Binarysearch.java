// CLI usage: 
// java Binarysearch 29/1-3-5-7-9-12-14-15-17-18-19-22-25-27-29-35-36-38-45-47-49-51-55-57-59-62-64-65-67-68-69
//
// File usage:
// 29
// 1 3 5 7 9 12 14 15 17 18 19 22 25 27 29 35 36 38 45 47 49 51 55 57 59 62 64 65 67 68 69

//
// Simple client for Binarysearch to be used in Threesum
// Read a target, and an array of sorted ints
// Binary Search for the target
// Return the target's index in array if present
// Return -1 if not present
//

package java1;

public class Binarysearch {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algsds/input/6binarysearch1.txt";
    
    private int Target;
    private int[] List;
    
    public Binarysearch() {

    }

    public Binarysearch(int target, int[] list) {
        Target = target;
        List = list;
    }

    private static void runClient(int[][] inputs) {
        int target = inputs[0][0];
        int[] list = inputs[1];
        Binarysearch bs = new Binarysearch(target, list);
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