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

}
