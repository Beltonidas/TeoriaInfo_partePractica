package Ej7_Enfermedades;

public class CondADadoB implements Condicion {

	private int A;
	private int B;

	public CondADadoB(int a, int b) {
		super();
		A = a;
		B = b;
	}

	@Override
	public boolean chequea(int a, int b) {
		return a == A && b == B;
	}

}
