//SuperClass
class SuperClass {
    int number=56;
}
//Subclass
class SubClass extends SuperClass {
    /*The same variable num is declared in the Subclass 
     *which is already present in the Superclass
    */
    int number=96;
    void printnumber(){
        System.out.println(number);
        System.out.println(super.number);
    }
}
class mainclass{
    public static void main(String args[]){
        SubClass sub = new SubClass();
        sub.printnumber();
    }
}
