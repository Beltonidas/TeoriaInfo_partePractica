package Ej7_Enfermedades;

import java.util.Scanner;

public class Ej7_3 {

	public static final int MIN_EXP = 200;

	private static double calcularProb(Condicion condicion) {

		int exitos = 0;
		int N = 0;
		double prob_ant = -1;
		double prob_act = 0;

		while (!converge(prob_act, prob_ant) || N < MIN_EXP) {

			int a = estaEnfermo();
			int b = resultadoTest(a);

			if (condicion.chequea(a, b)) {
				exitos++;
			}

			N++;

			prob_ant = prob_act;
			prob_act = (double) exitos / N;
		}
		return prob_act;
	}

	/**
	 * @param A puede ser 0 o 1 dependiendo de si esta enfermo o sano.
	 * @param B puede ser 0 o 1 dependiendo de si el test es positivo o negativo.
	 * 
	 * Primero calcula la probabilidad CONJUNTA de que se cumpla A y B,
	 * despues la probabilidad de B pero para esto necesita ambos valores que puede tomar A para B,
	 * es decir 0 con B y 1 con B: Consigue !AyB a partir de que tiene AyB.
	 * 
	 * @implNote P(B) = !AyB + AyB
	 
	 * @return Teorema de Bayes (probAyB / probB);
	 */
	public static double calcularCondicionalADadoB(int A, int B) {

		//que se cumpla A y B
		Condicion conjunta = new CondADadoB(A, B);
		
		//condicion !AyB
		Condicion complementaria = new CondADadoB(not(A), B);

		double probAyB = calcularProb(conjunta);
		double probB = calcularProb(complementaria) + probAyB; // P(B) = !AyB + AyB
		
		
		return (probAyB / probB); //Bayes

	}

	private static int not(int a) {
		if (a == 0) {
			return 1;
		}
		return 0;
	}

	static int estaEnfermo() {
		
		double[] prob_Acc = { 0.995, 1.0 }; // SANA = 0 y ENFERMA = 1
		double x = Math.random();

		if (x < prob_Acc[0]) {
			return 0;
		}

		return 1;
	}
	
	private static int resultadoTest(int a) {
		double[][] prob_Acc = { { 0.96, 0.05 },{ 1.0, 1.0 } };
		double x = Math.random();

		for (int i = 0; i <= 1; i++) { // documentar
			if (x < prob_Acc[i][a]) {
				return i;
			}
		}
		return 1;
	}

	static boolean converge(double prob_act, double prob_ant) {
		return ((double) (Math.abs((prob_ant - prob_act)) / prob_ant) < 0.000001);
	}


	
	//Main
	public static void main(String[] args) {

		System.out.println("SANO / NEGATIVO = 0 ");
		System.out.println("ENFERMO / POSITIVO = 1 ");

		Scanner leer = new Scanner(System.in);
		
		System.out.println("Cual es la probabilidad de que esté... ");
		int a = leer.nextInt();
		System.out.println("dado que dio... ");
		int b = leer.nextInt();
		
		
		System.out.println("Calculando la probabilidad P(PERSONA=" + a + "/TEST=" + b +") = "
				+ calcularCondicionalADadoB(a, b));

	}

}
