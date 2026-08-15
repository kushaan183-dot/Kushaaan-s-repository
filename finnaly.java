import java.util.Scanner;
public class finnaly {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.println("Enter 2 numbers: ");
            int y = sc.nextInt();
            int x = sc.nextInt();
            int z = y / x;  
            System.out.println(x +"/" + y + " = " + z);
        } catch (ArithmeticException ex) {
            System.out.println("-------catch block-------");
            System.out.println(ex);
        } finally {
            System.out.println("-------finally block-------");
            System.out.println("Application is designed & developed by: ");
            System.out.println("team @ Codingal");
        }
        System.out.println("DONE");
    }
}