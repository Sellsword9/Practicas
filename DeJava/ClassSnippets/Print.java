//No es util, pero me ayuda a practicar con Java
//ChatGPT ha cambiado el código para mejor

// import java.util.ArrayList; 
//Ya no hace falta el ArrayList
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Print {
    public static void ln(String s) {
        System.out.println(s); //Estos métodos no tienen fallos
    }
    public static void inline(String s) {
        System.out.print(s);
    }
    public static void ln(String s, Object... args) {
        System.out.println(Regex(s, args)); 
       // System.out.println(String.format(s, args));
       //ChatGPT quiere usar format porque no conoce el contexto de la práctica
    }
    
    private static String Regex(String s, Object... args) {
        String[] total = s.split("\\?"); //Hace falta escapar el "?"
        if (total.length - 1 != args.length) { //Ahorra código que faltaba
            throw new IllegalArgumentException("Number of placeholders does not match number of objects");
        }
        
        List<String> objStrs = //Prepara una lista objStrs
        Arrays.asList(args) //Pasa los args a una lista
        .stream() //A un stream
        .map(Object::toString) //Los convierte en String
        .collect(Collectors.toList()); //Los recoge en objStrs
        
        StringBuilder sb = new StringBuilder(); //Mejora la eficiciencia
        for (int i = 0; i < total.length; i++) {
            sb.append(total[i]);
            if (i < objStrs.size()) {
                sb.append(objStrs.get(i));
            }
        }
        return sb.toString();
    }
} 