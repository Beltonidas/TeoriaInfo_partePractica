package Ej7_SinReposicion;

import Ej7_ConReposicion.CondAlMenosUnTemaFacil;
import Ej7_ConReposicion.CondAmbosFaciles;
import Ej7_ConReposicion.CondUnTemaFacil;
import Ej7_ConReposicion.Condicion;

public class Ej7_2_SinReposicion {

	public static final int MIN_EXP = 160;

	static double calcularProb(Condicion condicion) {

		int exitos = 0;
		int N = 0;
		double prob_ant = -1;
		double prob_act = 0;

		while (!converge(prob_act, prob_ant) || N < MIN_EXP) {

			int a = PrimerTema();
			int b = SegundoTema(a);

			String t1 = convierteString(a);
			String t2 = convierteString(b);

			if (condicion.chequea(t1, t2)) {
				exitos++;

			}
			N++;

			prob_ant = prob_act;
			prob_act = (double) exitos / N;

		}

		return prob_act;

	}

	static int PrimerTema() {

		double[] prob_Acc = { 0.6, 1.0 };
		double x = Math.random();

		if (x < prob_Acc[0]) {
			return 0;
		}
		return 1;

		// retorna 0 para F y 1 para C
	}

	static int SegundoTema(int t1) {

		double[][] prob_Acc = { { 0.5, 0.75 }, 	// columna 0 salio tema facil
								{ 1.0, 1.0 } }; // columna 1 salio tema complejo
		double x = Math.random();

		for (int i = 0; i < 1; i++) {
			if (x < prob_Acc[i][t1]) {
				return i;
			}
		}
		return -1;

	}

	static boolean converge(double prob_act, double prob_ant) {
		return (Math.abs((double) (prob_ant - prob_act)) < 0.0001);
	}

	static String convierteString(int a) {

		if (a == 0) {
			return "F";
		}
		return "C";
	}

	// Main

	public static void main(String[] args) {

		Condicion A = new CondAlMenosUnTemaFacil();
		Condicion B = new CondUnTemaFacil();
		Condicion C = new CondAmbosFaciles();

		System.out.println("Calculando la probabilidad A).... " + calcularProb(A));
		System.out.println("Calculando la probabilidad B).... " + calcularProb(B));
		System.out.println("Calculando la probabilidad C).... " + calcularProb(C));

	}



	public class Montecarlo {
		private static final int MIN_MENSAJES = 500;
		private static final int NUM_SIMBOLOS = 3;
		// Valor Epsilon para control de convergencia
		private float epsilon = 0.000001f;
	
		// Constructor por defecto
		public Montecarlo()
		{
		}
	
		// Constructor con valor de epsilon
		public Montecarlo(float epsilon)
		{
			this.epsilon = epsilon;
		}
	
		private boolean Converge(float VoAnterior[], float VoActual[])
		{
			for(int i = 0; i < NUM_SIMBOLOS; i++){
				if(Math.abs(VoActual[i] - VoAnterior[i]) > this.epsilon){
					return false;
				}
			}
			return true;
		}
	
		private int Primer_Simbolo()
		{
			float[] VoAcumulada = new float[] {1f, 1f, 1f};
			float prob = (float) Math.random();
			for (int i = 0; i < NUM_SIMBOLOS; i++)
			{
				if (prob < VoAcumulada[i]) {
					return i;
				}
			}
			return -1;
		}
	
		private int Siguiente_Simbolo_Dado_Anterior(int simboloAnterior){
			float[][] matrizAcumulada = new float[][] {{1f/4,3f/4,0f}, {3f/4,1f,1f/2}, {1f,1f,1f}};
			float prob = (float) Math.random();
			for (int i = 0; i < NUM_SIMBOLOS; i++)
			{
				if (prob < matrizAcumulada[i][simboloAnterior]) {
					return i;
				}
			}
			return -1;
		}
	
		public float Calcular_Probabilidad_Emitir_Simbolo_Estado(int simbolo, int estado){
			int mensajes = 0;
			int[] emisiones = new int[] {0, 0, 0};
			float[] Vt = new float[] {0f, 0f, 0f};
			float[] Vt_Ant = new float[] {-1f, 0f, 0f};
			while(!this.Converge(Vt_Ant,Vt) || mensajes < MIN_MENSAJES)
			{
				int s = this.Primer_Simbolo();
				for(int i = 0; i < estado; i++){
					s = this.Siguiente_Simbolo_Dado_Anterior(s);
				}
				emisiones[s]++;
				mensajes++;
				for(int i = 0; i < NUM_SIMBOLOS; i++){
					Vt_Ant[i] = Vt[i];
					Vt[i] = (float)emisiones[i]/mensajes;
				}
			}
			return Vt[simbolo];
		}
	
		float [] mediaRecurrencia () {
			int[] ret_simbolos = {0, -1, -1};
			int tiempo_actual = 0;
			float[] mediaAct = {0, 0, 0};
			float[] mediaAnt = {-1, -1, -1};
			int s = Primer_Simbolo();
			while ((!this.Converge(mediaAnt, mediaAct)) || (tiempo_actual < MIN_MENSAJES)){
				s = this.Siguiente_Simbolo_Dado_Anterior(s);
				tiempo_actual++;
				ret_simbolos[s]++;
				mediaAnt[s] = mediaAct[s];
				mediaAct[s] = (float) tiempo_actual / ret_simbolos[s];
			}
			return mediaAct;
		}
	}

}
