
package DeJava.MoquitoHamcrest;

import java.util.List;

public class Instituto {
    private String nombre;
    private List<Alumno> alumnos;
    public Instituto(String nombre){
        
    }
    public String getNombre(){
        throw new UnsupportedOperationException("Sin programar");
    }
    
    public void añadir(Alumno a){
        alumnos.add(a);
    }
    
    public List<Alumno> getAlumnos(){
        return alumnos;
    }
}
