import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class GestorArchivos {
    private List<Integer> simbolos;
    private int matrizDato [][];


    public GestorArchivos() {
        this.simbolos = new ArrayList<>();
        matrizDato = null;
    }

    public void setMatrizDato(int[][] matrizDato) {
        this.matrizDato = matrizDato;
    }

    public void insertarOrdenado(int dato){
        if (simbolos.isEmpty()){
            simbolos.add(dato);
            return;
        }
        else{
            for (int i = 0; i < simbolos.size(); i++) {
                if (simbolos.get(i) > dato) {
                    simbolos.add(i, dato);
                    return;
                }
            }
        }
        simbolos.add(dato);
    }

    public void leerDatos(String ruta){
        try {
            BufferedReader entrada = new BufferedReader(new FileReader(ruta));
            String temp = "";
            String bfRead;

            while ((bfRead = entrada.readLine()) != null){
                // Leo la entrada
                temp= bfRead;
                // Opero con la entrada
                int datoParce = Integer.parseInt(temp);
                ordenarDatos(datoParce);
            }
        } catch (IOException e) {
            //No se encontro el archivo
            System.out.println("No se encontro el archivo");
        }
    }

    public void ordenarDatos(int dato){
        if(!simbolos.contains(dato)) {
            insertarOrdenado(dato);
        }
    }

    public int cantSimbolos(){
        return simbolos.size();
    }

    public void imprimirDatos(){
        for (int i = 0; i < simbolos.size(); i++) {
            System.out.print("->"+ simbolos.get(i));
        }
    }
}
