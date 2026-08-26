import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        System.out.print("How many names would you like to enter? ");
        int numberOfNames = Integer.parseInt(scanner.nextLine());

        for (int index = 0; index < numberOfNames; index++) {
            System.out.print("Enter name " + (index + 1) + ": ");
            names.add(scanner.nextLine());
        }

        System.out.print("Enter the name to find: ");
        String nameToFind = scanner.nextLine();

        names.forEach(name -> {
            if (name.equalsIgnoreCase(nameToFind)) {
                System.out.println("Eureka");
            }
        });

        scanner.close();
    }
}
