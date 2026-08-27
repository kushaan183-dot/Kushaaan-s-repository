import java.util.Scanner;

public class Multi-Catch {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		try {
			System.out.print("Enter first number: ");
			int x = Integer.parseInt(sc.nextLine());
			System.out.print("Enter second number: ");
			int y = Integer.parseInt(sc.nextLine());
			int z = x / y;
			System.out.println("Result: " + z);
		} catch (ArithmeticException | NumberFormatException exception) {
			System.out.println(exception);
		}
	}
}
