
package Clase;

import java.util.Random;

public record Empleado(int sueldo, String nombre ) {
    public String toString()
    {
        return nombre + ", que cobra " + sueldo + " y su numero favorito es el " + new Random().nextInt(0, 999);
    }
}
