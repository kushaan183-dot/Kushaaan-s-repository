class Mammals {
  void maam(){
    System.out.println("Inside Mammale class");
  }  
}
class Lion extends Mammals{
  void hum(){
    System.out.println("Inside Human class");
  }
}
class Human extends Mammals{
  void hum(){
    System.out.println("Inside Human class");
  }
}
class Mammles{
    public static void main(String[] args){
        Lion obj=new Lion();//object of child of child class
        obj.hum();//will make error as there is no Human objet
        obj.roar();
    }
}