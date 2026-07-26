import java.util.Scanner;

public class ReverseNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Input the number from the user
        System.out.print("Enter an integer to reverse: ");
        int number = scanner.nextInt();
        
        int originalNumber = number;
        int reversedNumber = 0;
        
        // Logic to reverse the number
        while (number != 0) {
            int remainder = number % 10;
            reversedNumber = reversedNumber * 10 + remainder;
            number = number / 10;
        }
        
        // Display the result
        System.out.println("Original Number: " + originalNumber);
        System.out.println("Reversed Number: " + reversedNumber);
        
        scanner.close();
    }
}
