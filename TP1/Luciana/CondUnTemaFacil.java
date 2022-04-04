
public class CondUnTemaFacil implements Condicion {

	@Override
	public boolean chequea(String t1, String t2) {
		return ((t1.equals("F") && t2.equals("C")) || (t1.equals("C") && t2.equals("F")));
	}

}
