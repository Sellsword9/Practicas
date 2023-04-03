//No es util, pero me ayuda a practicar con Java
import java.util.ArrayList;
import java.util.List;

public class Print {
    public static void ln(String s) {
        System.out.println(s);
    }
    public static void inline(String s) {
        System.out.print(s);
    }
    public static void ln(String s, List<Object> objects) {
        System.out.println(Regex(s, objects));
    }
    private static String Regex(String s, List<Object> objects) {
        String[] total;
        total = s.split("?");
        if (total.length == 1 && total[0].equals(s))
        {
            throw new IllegalArgumentException("String does not contain '?'");
        }
        List<String> objStrs = new ArrayList<>();
        objects.forEach(x -> objStrs.add(x.toString()));
        String superString = "";
        for (int i = 0; i<total.length; i++)
        {
            superString += total[i];
            superString += objStrs.get(i);
        }
        return superString;
    }
} 