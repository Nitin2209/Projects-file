class Thr extends Thread{
    public Thr(String name){
        super(name); 
    }

 public void run (){

    int i = 40;
   while (i<40) {  
    System.out.println("I am a Thread");
    i++;

   }
 }
}
public class main {

    public static void main(String[] args) {

        Thr t1 = new Thr("Nitn");
        Thr t2 = new Thr ("Nitin");
        t1.start();
        t2.start();
        System.out.println("The id of thread t is "+ t1.getId());
        System.out.println("The name of the thread t is " + t1.getName());
        System.out.println("The id of thread t is "+ t2.getId());
        System.out.println("The name of the thread t is " + t2.getName());
    }
}