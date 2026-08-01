class Parrent {
    int id,age;
    String name;
    void nameing(String name){
        System.out.println("Name is: "+name);
    }
}
class Child extends Parrent{
    void ageN(int age){
        System.out.println("Age of student is: "+age);
    }
}
class My_Inheritence{
    public static void main(String[] er){
        Child s=new Child();
        s.nameing("Aashish");
        s.ageN(14);
    }
}