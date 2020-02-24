package java1;

// CLI expected format "node myprog.js 1-2-3/4-5-6/7-8-9"
// to represent the file format:
// 1 2 3
// 4 5 6
// 7 8 9

public class Cli {

    public static String rowDelimiter = "/";
    public static String cellDelimiter = "-";

    public static int[][] readArgTo2DArray(String cliArg) {
        String[] lines = cliArg.split(rowDelimiter);
        int[][] array2D = new int[lines.length][];
        for (int i = 0; i < lines.length; i++) {
            String[] cells = lines[i].split(cellDelimiter);
            array2D[i] = new int[cells.length];
            for (int j = 0; j < cells.length; j++) {
                array2D[i][j] = Integer.parseInt(cells[j]);
            }
        }
        return array2D;
    }
}