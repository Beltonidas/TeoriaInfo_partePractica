public class Montecarlo {

    private static final int MIN = 10000;
    private float epsilon = 0.000001f;
    private int cant_simbolos = 3;

    public Montecarlo() {
    }

    public Montecarlo(float epsilon) {
        this.epsilon = epsilon;
    }

    public boolean converge(float ant[], float act[]) {
        for (int i = 0; i < act.length; i++) {
            if (Math.abs(ant[i] - act[i]) > this.epsilon) {
                return false;
            }
        }
        return true;
    }

    private boolean converge(float[][] act, float[][] ant) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 5; j++) {
                if (Math.abs(ant[i][j] - act[i][j]) > this.epsilon) {
                    return false;
                }
            }
        }
        return true;
    }

    public int Primer_simbolo() {
        float random = (float) Math.random();
        // 1 2 3 son los simbolos
        float[] Pacum = new float[] { 1f, 1f, 1f }; // Suponemos que arranca en el simbolo 1
        for (int i = 0; i < Pacum.length; i++) {
            if (random <= Pacum[i]) {
                return i;
            }
        }
        return -1; // No deberia pasar nunca
    }

    public int Siguiente_simbolo(int simb_ant) {
        float[][] matAcum = new float[][] { { 1f / 2, 1f / 3, 0f }, { 1f, 2f / 3, 1f }, { 1f, 1f, 1f } };
        float prob = (float) Math.random();
        for (int i = 0; i < this.cant_simbolos; i++) {
            if (prob <= matAcum[i][simb_ant]) {
                return i;
            }
        }
        return -1; // No deberia pasar nunca
    }

    public float[] Calcular_vector_estacionario() {
        int n = 0;
        int[] exitos = new int[] { 0, 0, 0 };
        float[] act = new float[] { 0f, 0f, 0f };
        float[] ant = new float[] { -1f, 0f, 0f };
        int s = this.Primer_simbolo();
        while (!converge(ant, act) || n < MIN) {
            int simb_ant = s;
            s = this.Siguiente_simbolo(simb_ant);
            exitos[s]++;
            n++;
            for (int i = 0; i < act.length; i++) {
                ant[i] = act[i];
                act[i] = (float) exitos[i] / n;
            }
        }
        return act;
    }

    float[][] Recurrencia() {
        int[][] retornos = { { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0 } };
        int tiempo_actual = 0;
        int[] total_retornos = { 0, 0, 0 };
        int[] ult_retorno = { -1, -1, -1 };
        float[][] f = { { 0f, 0f, 0f, 0f, 0f }, { 0f, 0f, 0f, 0f, 0f }, { 0f, 0f, 0f, 0f, 0f } };
        float[][] fant = { { -1f, 0f, 0f, 0f, 0f }, { -1f, 0f, 0f, 0f, 0f }, { -1f, 0f, 0f, 0f, 0f } };
        int s = this.Primer_simbolo();
        int aux = -1;
        while ((!this.converge(f, fant)) || (tiempo_actual < MIN)) {
            s = this.Siguiente_simbolo(s); // 0 , 1 , 2
            tiempo_actual++;
            if (ult_retorno[s] > 0) {
                total_retornos[s]++;
                aux = tiempo_actual - ult_retorno[s] - 1; // el -1 es para ubicarnos en el arreglo en la pos que debría
                if (aux < 5) {
                    retornos[s][aux]++;
                }
            }
            ult_retorno[s] = tiempo_actual; // ultimos retornos en el tiempo t, dado que esta inicializado

            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 5; j++) {
                    fant[i][j] = f[i][j];
                    f[i][j] = (float) retornos[i][j] / total_retornos[i]; // Copio la matriz y divido por la cantidad de
                                                                          // retornos
                }
            }
        }
        return f; // Retorno mi matriz
    }
}