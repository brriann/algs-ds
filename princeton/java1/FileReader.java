package java1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

// File format expected:
// 1 2 3
// 4 5 6
// 7 8 9

public class FileReader {

    public static String cellDelimiter = " ";

    public static int[][] readLinesTo2DArray(String filePath) {
        int[][] array2D;
        try {
            File file = new File(filePath);
            Scanner scanner = new Scanner(file);

            ArrayList<String> lines = new ArrayList<String>();
            while (scanner.hasNext()) {
                lines.add(scanner.nextLine());
            }
            array2D = new int[lines.size()][];
            for (int i = 0; i < lines.size(); i++) {
                String[] cells = lines.get(i).split(cellDelimiter);
                array2D[i] = new int[cells.length];
                for (int j = 0; j < cells.length; j++) {
                    array2D[i][j] = Integer.parseInt(cells[j]);
                }
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            array2D = new int[1][1];
        }
        return array2D;
    }
}