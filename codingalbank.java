import java.util.Scanner;
public class codingalbank {
    public static void main(String[] args) {
        boolean infiniteloop=true;
        double[] accountbalance=new double[1000];
        //this array contains the bank balence
        String[] accountname=new String[1000];
        // this array contains the  account owner name
        int opinion,size =100;//size will be the first account you want to begin from
        //infiniteloop keeps it runing till we stop it
        while(infiniteloop){
            System.out.println("Welcome to Codingal Banking Services");
            System.out.println("Banking menu:");
            System.out.println("Select any 1 option fr4om the below:");
            System.out.println("1-> add Costemer");
            System.out.println("2-> Change accounts name");
            System.out.println("3-> check accounts balence");
            System.out.println("4-> update accounts balence");
            System.out.println("5-> sumary of all accounts");
            System.out.println("6-> Quit");
            Scanner sc=new Scanner(System.in);
            System.out.println("To continue chouse your option");
            opinion=sc.nextInt();
            //we can even use switch case here instead of if 
            if(opinion==1){
                System.out.println("\nAdd Costemer \nMenu->");
                sc.nextLine();

                System.out.print("enter costemer name");
                String name=sc.nextLine();
                accountname[size]=name;
                System.out.print("Enter account opening balence");
                double amt=sc.nextDouble();
                accountbalance[size]=amt;
                System.out.println("Account created sucsessfuly. \n");
                System.out.println("Account details:- \n");
                System.out.println("Account number:-"+(size));
                System.out.println("Account name:-"+accountname[size]);
                System.out.println("Account balence:-"+accountbalance[size]+"Rs \n");
                System.out.println("==============================================");
                size=size+1;
            }else if(opinion==2){
                System.out.println("\n change costemer name menu");
                System.out.println("Enter account number:");
                //this is infact the logic of swapping
                int accountindex;
                String temp;

                accountindex=sc.nextInt();
                sc.nextLine();
                if(accountindex>size){
                    System.out.println("Account does not exist ");
                    System.out.println("Terminating");
                }else {
                    temp=accountname[accountindex];
                    System.out.print("enter the new name");
                    String name=sc.nextLine();
                    System.out.println("name sucsessfully updated from"+temp+"to"+name+".\n");
                }
            System.out.println("=========================");    
            }else if(opinion==3){
                System.out.println("\n /account balance");
                System.out.println("The Acount Balance is:"+accountbalance[size]);
            }else if(opinion==4){
                sc.nextLine();
                System.out.print("Enter account name: ");
                String searchname=sc.nextLine();
                int accountindex=-1;
                for(int index=100; index<size; index++){
                    if(accountname[index].equalsIgnoreCase(searchname)){
                        accountindex=index;
                        break;
                    }
                }
                if(accountindex == -1){
                    System.out.println("Account does not exist.");
                }else{
                    System.out.print("Enter new account balance: ");
                    double newbalance=sc.nextDouble();
                    accountbalance[accountindex]=newbalance;
                    System.out.println("Account balance updated successfully.");
                }
            }else if(opinion==5){
                System.out.println("\nSummary of all accounts:");
                if(size == 100){
                    System.out.println("No accounts have been created yet.");
                }else{
                    for(int accountindex = 100; accountindex < size; accountindex++){
                        System.out.println("Account number: " + accountindex);
                        System.out.println("Account name: " + accountname[accountindex]);
                        System.out.println("Account balance: " + accountbalance[accountindex] + " Rs");
                        System.out.println("============================================");
                    }
                }
            }else if(opinion==6){
                System.out.println("Thank you for using Codingal Banking Services.");
                infiniteloop=false;
            }
        }
    }
}
