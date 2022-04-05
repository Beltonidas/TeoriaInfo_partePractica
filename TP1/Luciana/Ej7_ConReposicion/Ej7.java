
public class Ej7 {

	public static final int MIN_EXP = 160;

	static double calcularProb(Condicion condicion) {

		int exitos = 0;
		int N = 0;
		double prob_ant = -1;
		double prob_act = 0;

		while (!converge(prob_act, prob_ant) || N < MIN_EXP) {

			String t1 = sacarTema();
			String t2 = sacarTema();

			if (condicion.chequea(t1, t2)) {
				exitos++;

			}
			N++;

			prob_ant = prob_act;
			prob_act = (double) exitos / N;

		}

		return prob_act;

	}

	static String sacarTema() {

		double[] prob_Acc = { 0.6, 1.0 };
		double x = Math.random();

		if (x < prob_Acc[0]) {
			return "F";
		}
		return "C";
	}

	static boolean converge(double prob_act, double prob_ant) {
		return (Math.abs((double) (prob_ant - prob_act)) < 0.0001);
	}

	
	//Main
	
	public static void main(String[] args) {

		Condicion A = new CondAlMenosUnTemaFacil();
		Condicion B = new CondUnTemaFacil();
		Condicion C = new CondAmbosFaciles();
		
		System.out.println("Calculando la probabilidad A).... " + calcularProb(A));
		System.out.println("Calculando la probabilidad B).... " + calcularProb(B));
		System.out.println("Calculando la probabilidad C).... " + calcularProb(C));

	}

}
