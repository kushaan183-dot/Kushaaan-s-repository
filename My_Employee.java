class Employee{
    int emplo;
    String name;
    float sal;

    Employee(){
        System.out.println("*****");
        emplo= 101;
        name="Aahshish";
        sal=5000f;
    }

    void displayDetails(){
        System.out.println(emplo + "|" + name +"|" + sal + "|");
    }
}
class My_Employee{
    public static void main(String[] args)
    {
        Employee emp1=new Employee();
        emp1.displayDetails();
    }
}