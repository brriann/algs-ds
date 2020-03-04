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

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/6binarysearch1.txt";
    
    private int Target;
    private int[] ListToSearch;
    
    public Binarysearch() {

    }

    public Binarysearch(int target, int[] list) {
        Target = target;
        ListToSearch = list;
    }

    public int search(int low, int high) {
        int foundIndex = -1;
        boolean found = false;
        int middle;

        while (low <= high && !found) {
            middle = low + ((high - low)) / 2;
            System.out.println(String.format("SEARCH lo hi: %d %d", low, high));
            System.out.println(String.format("cald\'d mid': %d", middle));
            if (ListToSearch[middle] > Target) {
                System.out.println("Go lower");
                high = middle - 1;
            } else if (ListToSearch[middle] < Target) {
                System.out.println("Go higher");
                low = middle + 1;
            } else {
                foundIndex = middle;
                found = true;
            }
        }
        return foundIndex;
    }

    private static void runClient(int[][] inputs) {
        int target = inputs[0][0];
        int[] list = inputs[1];

        Binarysearch bs = new Binarysearch(target, list);

        int initialLow = 0;
        int initialHigh = (list.length - 1);

        System.out.println(String.format("Initial lo hi: %d %d", initialLow, initialHigh));
        int targetIndex = bs.search(initialLow, initialHigh);

        // targetIndex = -1 for Not Found
        if (targetIndex < 0) {
            System.out.println("*** TARGET NOT IN LIST ***");
        } else {
            System.out.println(String.format("*** TARGET %d FOUND AT INDEX %d", target, targetIndex));
        }
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