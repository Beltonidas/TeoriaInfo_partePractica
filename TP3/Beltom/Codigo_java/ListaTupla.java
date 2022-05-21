import java.util.ArrayList;
import java.util.List;

public class ListaTupla {
    private List<Tupla> listTuplas;

    public ListaTupla() {
        this.listTuplas = new ArrayList<>();
    }

    public void addTupla(Tupla tupla){
        listTuplas.add(tupla);
    }

    public Tupla getTupla(int index){
        return listTuplas.get(index);
    }

    public void insertarOrdenado(Tupla tupla){
        for (int i = 0; i < listTuplas.size(); i++) {
            if (listTuplas.get(i).getProbabilidadSigno() < tupla.getProbabilidadSigno()){
                listTuplas.add(i, tupla);
                return;
            }
        }
        listTuplas.add(tupla);
    }

    public void removeAndSum(ListaCodigo listaCodigo){
        int index = listTuplas.size() -1;
        Tupla aux = listTuplas.get(index);
        Tupla aux2 = listTuplas.get(index-1);

        for (int i = 0; i < aux.getReferenciaPos().size(); i++) {
            int posCodigo = aux.getReferenciaPos().get(i);
            //System.out.println("Estoy agregando en la pos: "+ posCodigo);
            listaCodigo.agregarSimboloCodigo(posCodigo, 0);
        }
        for (int j = 0; j < aux2.getReferenciaPos().size(); j++) {
            int pos = aux2.getReferenciaPos().get(j);
            //System.out.println("Estoy agregando en la pos: "+ pos);
            listaCodigo.agregarSimboloCodigo(pos, 1);
        }
        //Sumo las tuplas
        double sum = aux.getProbabilidadSigno() + aux2.getProbabilidadSigno();
        //creo una nueva tupla
        Tupla nuevaTupla = new Tupla(sum);
        // Agrego las nuevas pociciones a las tuplas
        nuevaTupla.addPosicionesTupla(aux);
        nuevaTupla.addPosicionesTupla(aux2);
        listTuplas.remove(index);
        listTuplas.remove(index-1);
        insertarOrdenado(nuevaTupla);
        // Agrego la nueva tupla
    }

    public void imprimir(){
        for (int i = 0; i < listTuplas.size(); i++) {
            System.out.println(listTuplas.get(i).getProbabilidadSigno());
            System.out.println("---");
        }
    }

    public void ejecutar(ListaCodigo listaCodigo){
        while (listTuplas.size()>1)
            removeAndSum(listaCodigo);
    }
}
