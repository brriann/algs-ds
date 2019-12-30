
// compile this script with "javac Intro.java"
// invoke this script with an int array from CLI as "java Intro 0,1,2,3,4"

public class Intro {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("usage: java Intro x,y,z,a,b,c");
        } else {
            String[] arrayArgument = args[0].split(",");
            int[] arrayInt = new int[arrayArgument.length];
            for (int i = 0; i < arrayArgument.length; i++) {
                arrayInt[i] = Integer.parseInt(arrayArgument[i]);
            }
            int arraySum = 0;
            for (int i : arrayInt) {
                arraySum += i;
            }

            System.out.println(java.util.Arrays.toString(arrayInt));
            System.out.println("your array sum is:");
            System.out.println(arraySum);
        }
    }
}