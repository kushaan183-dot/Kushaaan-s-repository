class Student{
    int id;
    float stipend;
    String name;
    Student(){}
    Student(int id, String name){
        this.id=id;
        this.name=name;
    }
    Student(int id, String name, float stipend){
        this.id=id;
        this.name=name;
        this.stipend=stipend;
    }
    void displayDetails(){
        System.out.println("Id: "+this.id);
        System.out.println("Name: "+this.name);
        System.out.println("Stipend: "+this.stipend);
    }
}
class overloder{
    public static void main(String[] args) {
        Student s1=new Student();// defolt constructor
        Student s2=new Student(102,"Smith");// overloded constructor with 2 parameters
        Student s3=new Student(103,"David",3000);// overloded constructor with 3 parameters
        
        s1.displayDetails();
        s2.displayDetails();
        s3.displayDetails();
    }
}
