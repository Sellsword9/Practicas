package clases;

import java.io.Serializable;
import java.time.LocalDate;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

/*Cuando quiera que una clase se guarde en la base de datos;
    Tiro el @ a Entity,
    Implemento Serializable
*/

@Entity
public class Corredor implements Serializable {
    
    @Id @GeneratedValue private int id;
    private String nombre;
    private LocalDate fechaNacimiento;
    
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public LocalDate getFechaNacimiento() {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(LocalDate fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }

    
    public Corredor(){}
    public Corredor(String nombre, LocalDate fechaNacimiento)
    {
        this.nombre = nombre;
        this.fechaNacimiento = fechaNacimiento;
    }
}
