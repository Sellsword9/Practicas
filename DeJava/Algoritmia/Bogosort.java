package DeJava.Algoritmia;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Scanner; 
//Scanner import line can be commented for better performance? Consider it if faster times are needed
//La línea de importar el Scanner se podría comentar para optimizar, 

public class Bogosort {
    public static void main(String[] args) {
        final int PORDEFECTO = 500;
        System.out.println("Imput for size (1-1000 recommended)");
        System.out.println("Introduce el tamaño (1-1000 recomendado)");
        int Max = new Scanner(System.in).nextInt();
        if (Max <= 0) {Max = PORDEFECTO;}
        List<Integer> orden = new ArrayList<>();
        Random generator = new Random();
        for (int a : new int[Max]){
        orden.add(generator.nextInt(0, Integer.MAX_VALUE));}

        //List done
        //Lista hecha
        System.out.println("List:");
        orden.forEach(System.out::println);
        System.out.println("""
            --- End of list/Fin de lista
            --- Best time (Java)/
            ----Mejor tiempo con Java:  """);
        Collections.sort(orden);
    }
}
