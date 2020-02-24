// CLI usage: 
// java Intro x-y-z/a-b-c
//
// File usage:
// x y z 
// a b c

package java1;
import java.util.Arrays;

public class Intro {

    public static String INPUT_FILE_PATH = "/home/ubuntu/Dev/algs-ds/input/0intro3.txt";
    public static void main(String[] args) {
        if (args.length > 0) {
            introProgram(CliReader.readArgTo2DArray(args[0]));
        } else {
            introProgram(FileReader.readLinesTo2DArray(INPUT_FILE_PATH));
        }
    }

    private static void introProgram(int[][] array2D) {
        System.out.println("A.) Full 2D Array");
        System.out.println(Arrays.deepToString(array2D));
        System.out.println("B.) Each Row");
        for (int[] line : array2D) {
            System.out.println(Arrays.toString(line));
        }
        System.out.println("C.) Each Cell");
        for (int[] line : array2D) {
            for (int cell : line) {
                System.out.println(cell);
            }
        }
    }
}