import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        try {
            System.out.print("Enter first number x: ");
            int x = Integer.parseInt(sc.nextLine());

            System.out.print("Enter second number y: ");
            int y = Integer.parseInt(sc.nextLine());

            int z = x / y;
            System.out.println("Result: " + z);
        } catch (ArithmeticException e) {
            System.out.println("ArithmeticException: " + e);
        } catch (NumberFormatException e) {
            System.out.println("NumberFormatException: " + e);
        }

        // Bonus activity
        try {
            String[] items = new String[2];

            System.out.print("Enter first array item: ");
            items[0] = sc.nextLine();

            System.out.print("Enter second array item: ");
            items[1] = sc.nextLine();

            System.out.println("Third item: " + items[2]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBoundsException: " + e);
        }

        sc.close();
    }
}
