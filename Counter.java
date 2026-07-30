class Counter {
    int number=10;
    void increment() {
        number=number+1;
    }
    public static void main(String[] args) {
        Counter obj1=new Counter();
        obj1.increment();
        System.out.println(obj1.number);
    }
}
    

