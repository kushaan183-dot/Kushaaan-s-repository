import java.util.Scanner;

public class calculater {
    static class MathOperations {
        public void displayMessage() {
            System.out.println("Choose an operation:");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
        }
    }

    static class Addition extends MathOperations {
        public double add(double a, double b) {
            return a + b;
        }
    }

    static class Subtraction extends Addition {
        public double subtract(double a, double b) {
            return a - b;
        }
    }

    static class Multiplication extends Subtraction {
        public double multiply(double a, double b) {
            return a * b;
        }
    }

    static class Division extends Multiplication {
        public double divide(double a, double b) {
            if (b == 0) {
                System.out.println("Division by zero is not allowed.");
                return 0;
            }
            return a / b;
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        MathOperations menu = new MathOperations();
        menu.displayMessage();

        System.out.print("Enter your choice: ");
        int choice = input.nextInt();

        System.out.print("Enter first number: ");
        double num1 = input.nextDouble();
        System.out.print("Enter second number: ");
        double num2 = input.nextDouble();

        switch (choice) {
            case 1:
                Addition addObj = new Addition();
                System.out.println("Result of Addition: " + addObj.add(num1, num2));
                break;

            case 2:
                Subtraction subObj = new Subtraction();
                System.out.println("Result of Subtraction: " + subObj.subtract(num1, num2));
                break;

            case 3:
                Multiplication mulObj = new Multiplication();
                System.out.println("Result of Multiplication: " + mulObj.multiply(num1, num2));
                break;

            case 4:
                Division divObj = new Division();
                System.out.println("Result of Division: " + divObj.divide(num1, num2));
                break;

            default:
                System.out.println("Invalid choice. Please enter 1 to 4.");
                break;
        }

        input.close();
    }
}
