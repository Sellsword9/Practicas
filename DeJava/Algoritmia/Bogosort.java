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
        System.out.println("Imput for size (1-20 recommended)");
        System.out.println("Introduce el tamaño (1-20 recomendado)");
        Scanner sc = new Scanner(System.in);
        int Max = sc.nextInt();
        sc.close();
        if (Max <= 0) {Max = PORDEFECTO;}
        List<Integer> orden = new ArrayList<>();
        Random generator = new Random();
        for (int i = 0; i < Max; i++) {
            orden.add(generator.nextInt(0, Integer.MAX_VALUE));
        }
        
        //List done
        //Lista hecha
        System.out.println("List:");
        orden.forEach(System.out::println);
        //crea una copia de la lista orden
        //creates a copy of the list orden
        List<Integer> orden2 = new ArrayList<>(orden);
        
        System.out.println("""
            --- End of list/Fin de lista
            --- Best possible time (Java)/
            ----Mejor tiempo posible (con Java):  """);
        Collections.sort(orden);
        long duration = quicksort_time(orden);
        System.out.println(duration + " nanosegundos");
        
        long numeroIteraciones = 0;
        long timeLost = 0;
        long sumTimeStart = 0;
        long sumTimeEnd = 0;
        System.out.println("Bogosort time/Tiempo de bogosort: ");
        //Aquí empiezan los procesos del bogosort: Importante no añadir codigo innecesario para no afectar al tiempo
        long startTime = System.nanoTime();     
        while (!orden2.equals(orden2.stream().sorted().toList())) {
            sumTimeStart = System.nanoTime();
            numeroIteraciones = numeroIteraciones + 1;
            sumTimeEnd = System.nanoTime();
            timeLost += sumTimeEnd - sumTimeStart;
            Collections.shuffle(orden2);
        }
        long endTime = System.nanoTime(); //Aquí termina el proceso
        duration = (endTime - startTime - timeLost); 
        //Si la duración es mayor que x, para x = 10^18 nanosegundos, se muestra en segundos
        long x = 1000000000000000000L;
        if (duration > x) {
            System.out.println(duration / x + " segundos");
        } else {
            System.out.println(duration + " nanosegundos");
        }
        System.out.println("Number of iterations/Numero de iteraciones: " + numeroIteraciones);
    }
    
    
    
    
    /**
     * Devuelve el tiempo que se tarda en ordenar una lista con el método quicksort
     * @param orden La lista a ordenar
     * @return El tiempo que se tarda en ordenar la lista, en nanosegundos
     */
    private static long quicksort_time(List<Integer> orden) {
        long startTime = System.nanoTime();
        Collections.sort(orden);
        long endTime = System.nanoTime();
        long duration = (endTime - startTime);
        return duration;
    }
}