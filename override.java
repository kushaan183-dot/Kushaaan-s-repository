class Parent {
    public  void SayHello() {
        System.out.println("Hello from Parent");
    }
}
class Child extends Parent {
    @Override   
    public void SayHello() {
        System.out.println("Hello from Child");
    }
}

class override {

    public static void main(String[] args) {
        Parent p = new Parent(); // Output: Hello from Parent
        p.SayHello();
        Child c = new Child(); // Output: Hello from Child
        c.SayHello();
    }   
}