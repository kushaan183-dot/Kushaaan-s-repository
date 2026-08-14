interface Vehicle {
    // all are abstract methods.
    void changegear(int a);
    void speedup(int a);
    void applybrake(int a);
}
// we can inherit multiple interfaces using implements keyword
class Bicycle implements Vehicle {
    int speed;
    int gear;

    // to change gear
    @Override
    public void changegear(int newgear) {
        gear = newgear;
    }

    // to increase speed
    @Override
    public void speedup(int increment) {
        speed = speed + increment;
    }

    // to decrease speed
    @Override
    public void applybrake(int decrement) {
        speed = speed - decrement;
    }

    public void printstates() {
        System.out.println("speed: " + speed + " gear: " + gear);
    }
}
class car implements Vehicle {
    int speed;
    int gear;

    // to change gear
    @Override
    public void changegear(int newGear) {
        gear = newGear;
    }

    // to increase speed
    @Override
    public void speedup(int increment) {
        speed = speed + increment;
    }

    // to decrease speed
    @Override
    public void applybrake(int decrement) {
        speed = speed - decrement;
    }

    public void printstates() {
        System.out.println("speed: " + speed + " gear: " + gear);
    }
}
class Interface {
    public static void main(String args[]) {
        // creating an instance of Bicycle
        Bicycle bicycle = new Bicycle();
        bicycle.changegear(2);
        bicycle.speedup(3);
        bicycle.applybrake(1);

        System.out.println("Bicycle present state :");
        bicycle.printstates();
        
        // creating instance of car.
        car car = new car();
        car.changegear(1);
        car.speedup(4);
        car.applybrake(3);

        System.out.println("Car present state :");
        car.printstates();
    }
}