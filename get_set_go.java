class student{
    private String name;
    public String getName(){
        return name;
    }
    public  void Setname(String name){
        this.name=name;
    }
}
class get_set_go{
    public static void main(String[] args){
        student s=new student();
        s.Setname("Aashish @Codingal");
        System.out.println(s.getName());
    }
}