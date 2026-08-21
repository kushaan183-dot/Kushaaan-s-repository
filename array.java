import java.util.ArrayList;
class array {
    public static void main(String[] args){
        //creating an ArrayList of String type
        ArrayList<String> animals= new ArrayList<>();
        // adding elements
        animals.add("Lion");
        animals.add("Tiger");
        animals.add("Cheetah");
        System.out.println("======================Printing Current ArrayList======================");
        System.out.println(animals);
        System.out.println("The size of the Array:"+animals.size());
        System.out.println("Adding more elements:"+animals.add("Dog"));
        animals.remove(2);//removing the string at 2
        System.out.println(animals);
        animals.clear();
        System.out.println("======================Printing cleared array======================");
        System.out.print("Printing cleared array:"+animals);
        if(animals.isEmpty()){
            System.out.println("The array is empty");
        }
        else{
            System.out.println("The array is not empty");
        }
    }
}
