import java.util.ArrayList;
import java.util.List;

public class CodigoSimple {
    private List<Integer> codigoBinario;
    private Tupla tuplaAsociada;

    public CodigoSimple() {
        this.codigoBinario = new ArrayList<>();
    }

    public CodigoSimple(List<Integer> codigoBinario, Tupla tuplaAsociada) {
        this.codigoBinario = codigoBinario;
        this.tuplaAsociada = tuplaAsociada;
    }

    public List<Integer> getCodigoBinario() {
        return codigoBinario;
    }

    public void setCodigoBinario(List<Integer> codigoBinario) {
        this.codigoBinario = codigoBinario;
    }

    public void setBitCodigo(Integer bit) {
        codigoBinario.add(bit);
    }

    public void imprimirCodigo(){
        int pos = codigoBinario.size() -1;
        while (pos >=0){
            System.out.println(codigoBinario.get(pos) + "--> ");
            pos--;
        }
        System.out.println("----------------------------------------- ");
    }

}
