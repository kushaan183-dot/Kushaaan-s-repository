interface Myinterface {
    /* compiler will treat them as:
    * public abstract void method1();
    * public abstract void method2();
    */
    public void method1();
    public void method2();
}
class MyInterface implements Myinterface {
    // implementing the abstract methods
    @Override
    public void method1() {
        System.out.println("Implementation of method1");
    }

    @Override
    public void method2() {
        System.out.println("Implementation of method2");
    }

    public static void main(String args[]) {
        MyInterface obj = new MyInterface();
        obj.method1();
        obj.method2();
    }
}

