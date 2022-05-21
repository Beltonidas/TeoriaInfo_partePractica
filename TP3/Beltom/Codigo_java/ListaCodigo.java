import java.util.ArrayList;
import java.util.List;

public class ListaCodigo {
    private List<CodigoSimple> listaCodigos;

    public ListaCodigo() {
        this.listaCodigos = new ArrayList<>();
    }

    public void agregarCodigoSimple(CodigoSimple codigoSimple){
        listaCodigos.add(codigoSimple);
    }

    public void agregarSimboloCodigo(int pos, int bit){
        listaCodigos.get(pos).setBitCodigo(bit);
    }

    public CodigoSimple getCodigoSimple (int pos){
        return listaCodigos.get(pos);
    }
}
