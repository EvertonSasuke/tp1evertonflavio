package parque;

public class Gato {
    public String name;
    public String breed;
    public int isAge;
    public boolean isMale = false;
    Gato registration;
    public Gato(String name){
        this.name = name;
    }
    
    public void Miar(){
        System.out.printf("\n%s: Miau, miau, miau.", this.name);
    }
}
