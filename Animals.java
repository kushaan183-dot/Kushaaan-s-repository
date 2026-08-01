class Animal{
    void eat(){
        System.out.println("Eating...Animal class...roar method");
    }

}
class Lion extends Animal{
    void roar(){
        System.out.println("Roar...Loin class...roar method");
    }
}
class BabylLion extends Lion{
    void baby(){
        System.out.println("weeping...BabylLion class...weep method");
    }
}
class Animals{
    public static void main(String[] args){
        BabylLion obj=new BabylLion();//object of child of child class
        obj.eat();
        obj.roar();
        obj.baby();
    }

}