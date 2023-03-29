package Clase;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Stream;
import java.util.Random;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Programa {

    static List<String> palabras = List.of("Lunes",
            "Martes", "Miercoles", "Jueves", "Viernes");
    private static List<Departamento> departamentos
                = List.of(
                        new Departamento("Informático",
                                List.of(
                                        new Empleado(100, "Antonio"),
                                        new Empleado(900, "Paco"),
                                        new Empleado(1800, "Pancarcho")
                                )),
                        new Departamento("Otro depar",
                                List.of(
                                        new Empleado(100, "Paco2"),
                                        new Empleado(18000, "Yeray")
                                )),
                        new Departamento("Metalurgia",
                                List.of(
                                        new Empleado(2100, "Erlound"),
                                        new Empleado(8000, "Kodlack")
                                )
                        ));
    public static void main(String[] args) {

        Random rd = new Random();
        IntStream.generate(() -> rd.nextInt(0, 500))
                .limit(1000)
                .distinct()
                .map(x -> x * x)
                .sum();

        //main2(args);
        main3(args);
    }

    public static void main2(String[] args) {
        
        System.out.println(palabras
                .stream()
                .collect(Collectors.joining(",")));
    }

    public static void main3(String args[]) {
        
        departamentos
                .stream()
                .flatMap(x -> x.getEmpleados().stream())
                .filter(x -> x.sueldo()>999)
                .forEach(System.out::println);
        
    }

}
