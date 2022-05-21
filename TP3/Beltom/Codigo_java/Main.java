import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        System.out.println("Good nigth...");


        /*try {
            FileReader entrada = new FileReader("C:\\GitHub\\Teoria_Informacion\\Beethoven.txt");
            int c = entrada.read();
            while (c!= -1){
                // Leo la entrada
                c= entrada.read();

                // Opero con la entrada
                System.out.println("--> "+ c);
            }
        } catch (IOException e) {
            //No se encontro el archivo
            System.out.println("No se encontro el archivo");
        }*/
        GestorArchivos gestorArchivos = new GestorArchivos();
        gestorArchivos.leerDatos("C:/GitHub/Teoria_Informacion/L-gante.txt");
        System.out.println(gestorArchivos.cantSimbolos());
        gestorArchivos.imprimirDatos();
        int cantidadSimbolos = gestorArchivos.cantSimbolos();
        int matrizDatos[][] = new int[2][cantidadSimbolos];
        gestorArchivos.setMatrizDato(matrizDatos);


        /*ListaTupla listTuplas = new ListaTupla();
        Tupla tupla1 = new Tupla(0.5);
        tupla1.addPos(0);

        Tupla tupla2 = new Tupla(0.2);
        tupla2.addPos(1);

        Tupla tupla3 = new Tupla(0.1);
        tupla3.addPos(2);

        Tupla tupla4 = new Tupla(0.1);
        tupla4.addPos(3);

        Tupla tupla5 = new Tupla(0.1);
        tupla5.addPos(4);

        listTuplas.addTupla(tupla1);
        listTuplas.addTupla(tupla2);
        listTuplas.addTupla(tupla3);
        listTuplas.addTupla(tupla4);
        listTuplas.addTupla(tupla5);



        CodigoSimple code1 = new CodigoSimple();
        CodigoSimple code2 = new CodigoSimple();
        CodigoSimple code3 = new CodigoSimple();
        CodigoSimple code4 = new CodigoSimple();
        CodigoSimple code5 = new CodigoSimple();
        ListaCodigo listCodigos = new ListaCodigo();
        listCodigos.agregarCodigoSimple(code1);
        listCodigos.agregarCodigoSimple(code2);
        listCodigos.agregarCodigoSimple(code3);
        listCodigos.agregarCodigoSimple(code4);
        listCodigos.agregarCodigoSimple(code5);*/


        /*listTuplas.ejecutar(listCodigos);


        System.out.println("----Los codigos---");
        listCodigos.getCodigoSimple(0).imprimirCodigo();
        listCodigos.getCodigoSimple(1).imprimirCodigo();
        listCodigos.getCodigoSimple(2).imprimirCodigo();
        listCodigos.getCodigoSimple(3).imprimirCodigo();
        listCodigos.getCodigoSimple(4).imprimirCodigo();
*/



    }
}
