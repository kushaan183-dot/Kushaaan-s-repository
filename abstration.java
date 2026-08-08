abstract class object {
    abstract void showShape();
    public void shape(){
        System.out.println("TI am in an abstract class");
    }
}
class Sphere extends object{
    /**
*this is indirectly a overrideen showshape method by
making use of abstract class
*/
    void showShape(){
        System.out.println("I am a Sphere");
    }
}
class Cuboid extends object{
    /**
*this is indirectly a overrideen showshape method by
making use of abstract class 
*/
    void showShape(){
        System.out.println("I am a Cuboid");
    }
}
class Prism extends object{
        /**
*this is indirectly a overrideen showshape method by
making use of abstract class 
*/
    void showShape(){
        System.out.println("I am a Prism");
    }
}
class abstration{
    public static void main(String args[]){
        object obj=new Sphere();
        obj.showShape();
        obj=new Cuboid();
        obj.showShape();
        obj=new Prism();
        obj.showShape();
        obj.shape();
    }
}