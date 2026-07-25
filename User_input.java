import java.util.*;
class User_input {
    public static void main(String[] args) {
        int sum=0;
        String result;
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of Subjects you want to add:");
        int noOfSubjects=sc.nextInt();
        int marks[]=new int[noOfSubjects];// initializing array 
        System.out.println("Enter the marks of "+noOfSubjects+" subjects:");
        // entering the marks of subjects
        for(int i=0;i<noOfSubjects;i++){
            marks[i]=sc.nextInt();
        }//calculating the sum of marks
        for(int j=0;j<noOfSubjects;j++){
            sum+=marks[j];
        }// generating the result based on the sum of marks
        int percentage=sum/noOfSubjects;
        if(percentage>=95){
            result="A+";
        }
        else if(percentage>=75 && percentage<95){
            result="A";
        }
        else if(percentage>=65 && percentage<75){
            result="B+";
        }
        else if(percentage>=55 && percentage<65){
            result="B";
        }
        else if(percentage>=45 && percentage<55){
            result="C";
        }
        else{
            result="Fail";
        }
        System.out.println("the result is: "+result);
        System.out.println("the percentage is: "+percentage);
    }
}