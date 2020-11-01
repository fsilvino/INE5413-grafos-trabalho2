from GrafoDirigido import GrafoDirigido
from GrafoNaoDirigido import GrafoNaoDirigido
from OrdenacaoTopologica import OrdenacaoTopologica
from ArvoreGeradoraMinima import ArvoreGeradoraMinima
from ComponentesFortementeConexos import ComponentesFortementeConexos

class GrafoExecutor:

    def buscarComponentesFortementeConexos(grafo: GrafoDirigido):
        componentes = ComponentesFortementeConexos.buscarComponentesFortementeConexos(grafo)
        ComponentesFortementeConexos.mostrarComponentes(componentes)

    def ordenacaoTopologica(grafo: GrafoDirigido):
        lista = OrdenacaoTopologica.ordenar(grafo)
        OrdenacaoTopologica.mostrarOrdenacaoTopologica(lista)

    def montarArvoreGeradoraMinima(grafo: GrafoNaoDirigido):
        a = ArvoreGeradoraMinima.montarArvoreGeradoraMinima(grafo)
        ArvoreGeradoraMinima.mostrarAGM(a)


    buscarComponentesFortementeConexos = staticmethod(buscarComponentesFortementeConexos)
    ordenacaoTopologica = staticmethod(ordenacaoTopologica)
    montarArvoreGeradoraMinima = staticmethod(montarArvoreGeradoraMinima)