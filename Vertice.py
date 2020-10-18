from Aresta import Aresta
from Relacao import Relacao

class Vertice:

    def __init__(self, numero, rotulo):
        self.numero = numero
        self.rotulo = rotulo
        self.arestas = {}

    def adicionarAresta(self, relacao:Relacao):
        self.arestas[relacao.uid] = relacao

    def ehVizinhoDe(self, v2):
        return self.encontrarArestaPara(v2) != None

    def encontrarArestaPara(self, v2):
        idAresta = Relacao.gerarIdRelacao(self, v2)
        if (idAresta in self.arestas):
            return self.arestas[idAresta]
        return None
