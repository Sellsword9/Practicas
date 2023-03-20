package clases;

import java.time.LocalDate;
import javax.persistence.EntityManager;
import javax.persistence.Persistence;

public class Pograma {
    public static void main(String[] args) {
     EntityManager em = Persistence.createEntityManagerFactory("CARRERA").createEntityManager();
     
     Corredor c = new Corredor("Alvaro", LocalDate.now().minusYears(20));
     
     
     
     
     em.close();
    }
}
