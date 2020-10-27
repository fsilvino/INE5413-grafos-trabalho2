from Grafo import Grafo
from OrdenacaoTopologica import OrdenacaoTopologica

class GrafoExecutor:

    def qtdVertices(self, grafo:Grafo):
        grafo.validarSeFoiCarregado()
        return grafo.numeroDeVertices

    def qtdRelacoes(self, grafo:Grafo):
        grafo.validarSeFoiCarregado()
        return grafo.numeroDeRelacoes

    def grau(self, grafo:Grafo,  v):
        grafo.validarSeFoiCarregado()
        return len(grafo.vertices[v - 1].relacoes)

    def rotulo(self, grafo:Grafo, v):
        grafo.validarSeFoiCarregado()
        return grafo.vertices[v - 1].rotulo

    def vizinhos(self, grafo:Grafo, v):
        grafo.validarSeFoiCarregado()
        vertice = grafo.vertices[v - 1]
        return list(map(lambda r: r.obterOutraParte(vertice), vertice.relacoes.values()))

    def haRelacao(self, grafo:Grafo, u, v):
        grafo.validarSeFoiCarregado()
        return grafo.vertices[u - 1].ehVizinhoDe(grafo.vertices[v - 1])

    def peso(self, grafo:Grafo, u, v):
        grafo.validarSeFoiCarregado()
        relacao = grafo.vertices[u - 1].encontrarRelacaoPara(grafo.vertices[v - 1])
        return relacao.peso if relacao != None else float("inf")

    def ordenacaoTopologica(self, grafo:Grafo):
        grafo.validarSeFoiCarregado()
        ord = OrdenacaoTopologica()
        return ord.ordenar(grafo)
