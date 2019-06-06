package parque;

public class Parque {

    public static void main(String[] args) {
        Gato instance1 = new Gato("Yugi");
        instance1.breed = "Ragdoll";
        instance1.isAge = 4;
        instance1.isMale = true;
        instance1.Miar();

        Gato instance2 = new Gato("Téa");
        instance2.breed = "Birman";
        instance2.isAge = 3;
        instance2.isMale = false;
        instance2.Miar();
    }
    
}
