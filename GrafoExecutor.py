from Grafo import Grafo
from GrafoDirigido import GrafoDirigido
from OrdenacaoTopologica import OrdenacaoTopologica
from ArvoreGeradoraMinima import ArvoreGeradoraMinima
from ComponentesFortementeConexos import ComponentesFortementeConexos

class GrafoExecutor:

    def qtdVertices(self, grafo:Grafo):
        return grafo.numeroDeVertices

    def qtdRelacoes(self, grafo:Grafo):
        return grafo.numeroDeRelacoes

    def grau(self, grafo:Grafo,  v):
        return len(grafo.vertices[v - 1].relacoes)

    def rotulo(self, grafo:Grafo, v):
        return grafo.vertices[v - 1].rotulo

    def vizinhos(self, grafo:Grafo, v):
        vertice = grafo.vertices[v - 1]
        return list(map(lambda r: r.obterOutraParte(vertice), vertice.relacoes.values()))

    def haRelacao(self, grafo:Grafo, u, v):
        return grafo.vertices[u - 1].ehVizinhoDe(grafo.vertices[v - 1])

    def peso(self, grafo:Grafo, u, v):
        relacao = grafo.vertices[u - 1].encontrarRelacaoPara(grafo.vertices[v - 1])
        return relacao.peso if relacao != None else float("inf")

    def ordenacaoTopologica(self, grafo:Grafo):
        ord = OrdenacaoTopologica()
        lista = ord.ordenar(grafo)
        ord.show_result(lista)
        # return ord.ordenar(grafo)

    def montarArvoreGeradoraMinima(self, grafo:Grafo):
        arvore = ArvoreGeradoraMinima()
        a = arvore.montarArvoreGeradoraMinima(grafo)
        arvore.show_result(a)

    def buscarComponentesFortementeConexos(self, grafo:Grafo):
        con = ComponentesFortementeConexos()
        listaAncestrais = con.buscarComponentesFortementeConexos(grafo)
        arvores = con.buscarArvoresCompFortConexos(listaAncestrais)
        con.show_result(arvores)
