import java.util.Scanner;

public class ReportCard {
    static final int WIDTH = 48;

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter student name: ");
        String name = input.nextLine();

        System.out.print("Enter class: ");
        String studentClass = input.nextLine();

        String[] subjects = {
                "English",
                "Mathematics",
                "Social Science",
                "Chemistry",
                "Physics"
        };

        double[] marks = new double[subjects.length];
        double total = 0;

        for (int i = 0; i < subjects.length; i++) {
            System.out.print("Enter marks for " + subjects[i] + ": ");
            marks[i] = input.nextDouble();
            total += marks[i];
        }

        double percentage = (total / (subjects.length * 100)) * 100;

        System.out.println();
        System.out.println(centerText("REPORT CARD", WIDTH));
        System.out.println();
        System.out.println(centerText("NAME:", WIDTH));
        System.out.println(centerText(name, WIDTH));
        System.out.println();
        System.out.println(centerText("SUBJECT           MARK", WIDTH));

        for (int i = 0; i < subjects.length; i++) {
            System.out.println(centerText(String.format("%-18s %5.2f", subjects[i], marks[i]), WIDTH));
        }

        System.out.println();
        System.out.println(centerText("TOTAL: " + String.format("%.2f", total), WIDTH));
        System.out.println(centerText(String.format("AVERAGE: %.2f", percentage), WIDTH));
    }

    public static String centerText(String text, int width) {
        if (text.length() >= width) {
            return text;
        }

        int leftPadding = (width - text.length()) / 2;
        int rightPadding = width - text.length() - leftPadding;

        return " ".repeat(leftPadding) + text + " ".repeat(rightPadding);
    }
}
