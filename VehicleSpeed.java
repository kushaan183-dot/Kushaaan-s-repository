import java.util.Scanner;

public class VehicleSpeed {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter vehicle type (Truck/Bike): ");
        String vehicle = sc.nextLine().trim().toLowerCase();
        System.out.print("Enter current gear (1-5): ");
        int gear = Integer.parseInt(sc.nextLine().trim());
        System.out.print("Enter brakes applied (0-3): ");
        int brakes = Integer.parseInt(sc.nextLine().trim());

        int baseSpeed = switch (vehicle) {
            case "truck" -> 60;
            case "bike" -> 30;
            default -> {
                System.out.println("Invalid vehicle type.");
                yield 0;
            }
        };

        if (baseSpeed == 0) return;

        int speed = baseSpeed + (gear * 10) - (brakes * 15);
        if (speed < 0) speed = 0;

        System.out.println(vehicle + " current speed is: " + speed + " km/h");
        sc.close();
    }
}
