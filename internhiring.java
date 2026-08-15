import java.util.Scanner;

public class internhiring {
    public static Candidate getCandidatedetails() throws InvalidInternException {
    Scanner scanner = new Scanner(System.in);
    // we are creating a hiring tool where the HR can regsiter candidates based on eligibilty to the databse
    //databse connection is not done in this program to avoid complexity at this point of time
    //this could be completed using simple if else too but when systems become complex and big using the standard approach becomes the best solution
    System.out.println("Enter the candidate name: ");
    System.out.println("Name");
    String name= scanner.next();
    System.out.println("Gender");
    String gender = scanner.next();
    System.out.println("Enter persentage in 10th");
    int persentage=scanner.nextInt();
    //extra eligibilty criteria can also be added based on the understanding
    //12th marks
    //does skills contains Java
    if(persentage<50){
        scanner.close();
        throw new InvalidInternException("Candidate is not eligible for internship");
        }else{
            Candidate candidate = new Candidate(name, persentage);
            candidate.setname(name);
            candidate.setpersentage(persentage);
            candidate.setgender(gender);
            scanner.close();
            return candidate;
        }   
    }
    public static void main(String[] args){
        System.out.println("Welcome to the Intern Hiring Tool");
        try{
            Candidate candidate = getCandidatedetails();
            System.out.println("Successfully hired: " + candidate.toString());
        }catch(InvalidInternException e){
            System.out.println(e.getMessage());
        }
    }
}
public class Candidate{
    private String name;
    private int percentage;
    private String gender;
    public string getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getPercentage() {
        return percentage;
    }
    public void setPercentage(int percentage) {
        this.percentage = percentage;
    }
    public String getGender() {
        return gender;
    }
    public void setGender(String gender) {
        this.gender = gender;
    }

}
//InvalidInternException.java
public class InvalidInternException extends Exception {
    public InvalidInternException(String message) {
        super(message);
    }
}