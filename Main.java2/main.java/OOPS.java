class Bass {

    int x;
    public int getx(){
        return x;
    }
    public void setx(int x){
        System.out.println("I am setting x now");
        this.x = x;
    }
    public void printme(){
        System.out.println("I am a constructer");
    }
}
    class Drived extends Bass{
        int y ;
        public int gety() {
            return y;
        }
        public void sety(){
            int y;
        }

        public class OOPS {
        
            public static void main(String[] args) {
                Bass b = new Bass();
                b.setx(5);
                System.out.println (b.getx());
                
            }
        }
    
    }
