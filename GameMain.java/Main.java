
import java.util.Random;
import java.util.Scanner;

public class Main {
    
      public static void main(String[] args) {
         int rocke = 0;
         int Paper = 1;
         int Scissor = 2;
         
        Scanner sc = new Scanner(System.in);
        int user = sc.nextInt();

        Random rnd = new Random();
        int computer = rnd.nextInt(3);
        
        if (user==0) {
          System.out.println("Human choice rocke");
        }
        else if (user==1) {
          System.out.println("Human choice paper");
        }
        else if(user==2){
          System.out.println("Human choice scissor");
        }
        else if(user<0){
          System.out.println("invalid choice \n choose only under 0,1,2");
        }
        else if (user>2) {
          System.out.println("invalid choice \n choose only under 0,1,2");
        }
        if (computer==0) {
          System.out.println("computer choice is rocke");          
        }
        else if (computer==1) {
          System.out.println("computer choice is paper");
        }
        else if (computer==2) {                                                                     
          System.out.println("computer choice is scissor");
        }
        if (computer==user) {
          System.out.println("Drow or no one wins or no one lose");
        }
        else if (computer==0&& user==1 || computer==1&& user==2 || computer==2&& user==0 ) {
          System.out.println("Human wins");
        }
        else if (computer==1&& user==0 || computer==2&& user==1 || computer==0&& user==2) {
          System.out.println("computer wins");
        }
       if (user<0) {
          System.out.println("??");
        } 
        else if (user>2) {
          System.out.println("??");
        }

      }
    }
    

