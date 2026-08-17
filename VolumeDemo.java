import java.util.Scanner;

public class VolumeDemo {
    static abstract class Shape {
        public abstract double getVolume();
    }

    static class Cube extends Shape {
        private double side;

        public Cube(double side) {
            setSide(side);
        }

        public double getSide() {
            return side;
        }

        public void setSide(double side) {
            if (side < 0) {
                throw new IllegalArgumentException("Side cannot be negative.");
            }
            this.side = side;
        }

        @Override
        public double getVolume() {
            return side * side * side;
        }
    }

    static class Cuboid extends Shape {
        private double length;
        private double breadth;
        private double height;

        public Cuboid(double length, double breadth, double height) {
            setLength(length);
            setBreadth(breadth);
            setHeight(height);
        }

        public double getLength() {
            return length;
        }

        public void setLength(double length) {
            if (length < 0) {
                throw new IllegalArgumentException("Length cannot be negative.");
            }
            this.length = length;
        }

        public double getBreadth() {
            return breadth;
        }

        public void setBreadth(double breadth) {
            if (breadth < 0) {
                throw new IllegalArgumentException("Breadth cannot be negative.");
            }
            this.breadth = breadth;
        }

        public double getHeight() {
            return height;
        }

        public void setHeight(double height) {
            if (height < 0) {
                throw new IllegalArgumentException("Height cannot be negative.");
            }
            this.height = height;
        }

        @Override
        public double getVolume() {
            return length * breadth * height;
        }
    }

    static class Cylinder extends Shape {
        private double radius;
        private double height;

        public Cylinder(double radius, double height) {
            setRadius(radius);
            setHeight(height);
        }

        public double getRadius() {
            return radius;
        }

        public void setRadius(double radius) {
            if (radius < 0) {
                throw new IllegalArgumentException("Radius cannot be negative.");
            }
            this.radius = radius;
        }

        public double getHeight() {
            return height;
        }

        public void setHeight(double height) {
            if (height < 0) {
                throw new IllegalArgumentException("Height cannot be negative.");
            }
            this.height = height;
        }

        @Override
        public double getVolume() {
            return Math.PI * radius * radius * height;
        }
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Choose a shape to calculate volume:");
        System.out.println("1. Cube");
        System.out.println("2. Cuboid");
        System.out.println("3. Cylinder");
        System.out.print("Enter your choice: ");

        int choice = input.nextInt();

        switch (choice) {
            case 1:
                System.out.print("Enter the side of cube: ");
                double cubeSide = input.nextDouble();
                Shape cube = new Cube(cubeSide);
                System.out.println("Volume of cube = " + cube.getVolume());
                break;

            case 2:
                System.out.print("Enter length: ");
                double length = input.nextDouble();
                System.out.print("Enter breadth: ");
                double breadth = input.nextDouble();
                System.out.print("Enter height: ");
                double height = input.nextDouble();
                Shape cuboid = new Cuboid(length, breadth, height);
                System.out.println("Volume of cuboid = " + cuboid.getVolume());
                break;

            case 3:
                System.out.print("Enter radius: ");
                double radius = input.nextDouble();
                System.out.print("Enter height: ");
                double cylinderHeight = input.nextDouble();
                Shape cylinder = new Cylinder(radius, cylinderHeight);
                System.out.println("Volume of cylinder = " + cylinder.getVolume());
                break;

            default:
                System.out.println("Invalid choice. Please select 1, 2, or 3.");
                break;
        }

        input.close();
    }
}
