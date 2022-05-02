public class Main {
    public static void main(String[] args) {
        Montecarlo m = new Montecarlo();
        int cant_pruebas = 4;

        System.out.println("Vector Estacionario");
        for (int i = 1; i <= cant_pruebas; i++) {
            float[] prob = m.Calcular_vector_estacionario();
            System.out.print("[Prueba" + i + "]: ");
            for (int j = 0; j < prob.length; j++) {
                System.out.print(prob[j] + " ");
            }
            System.out.println("");
        }

        System.out.println("");

        System.out.println("Matriz de Recurrencia");
        float[][] recu = m.Recurrencia();
        for (int i = 0; i < 3; i++) {
            System.out.print("Simbolo " + (i + 1) + ": ");
            for (int j = 0; j < 5; j++) {
                System.out.print(recu[i][j] + " ");
            }
            System.out.println(" ");
        }
    }
}