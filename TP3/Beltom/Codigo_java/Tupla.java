import java.util.ArrayList;
import java.util.List;

public class Tupla {
    private double probabilidadSigno;
    private List<Integer> referenciaPos;

    public Tupla(double probabilidadSigno) {
        this.probabilidadSigno = probabilidadSigno;
        this.referenciaPos = new ArrayList<>();
    }

    public void setProbabilidadSigno(double prob){
        probabilidadSigno = prob;
    }
    public double getProbabilidadSigno(){
        return probabilidadSigno;
    }

    public void addPos(int pos){
        referenciaPos.add(pos);
    }

    public List<Integer> getReferenciaPos (){
        return  referenciaPos;
    }

    public int getElementPost(int index){
        return referenciaPos.get(index);
    }

    public void addPosicionesTupla (Tupla tupla){
        for (int i = 0; i < tupla.getReferenciaPos().size(); i++) {
            referenciaPos.add(tupla.getElementPost(i));
        }
    }

    public void imprimirPosicionTuplas (){
        for (int i = 0; i < referenciaPos.size(); i++) {
            System.out.println(" - "+ referenciaPos.get(i) );
        }
    }
}
