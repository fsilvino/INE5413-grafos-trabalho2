from Aresta import Aresta
from Relacao import Relacao

class Vertice:

    def __init__(self, numero, rotulo):
        self.numero = numero
        self.rotulo = rotulo
        self.relacoes = {}

    def adicionarRelacao(self, relacao:Relacao):
        self.relacoes[relacao.uid] = relacao

    def ehVizinhoDe(self, v2):
        return self.encontrarRelacaoPara(v2) != None

    def encontrarRelacaoPara(self, v2):
        idRelacao = Relacao.gerarIdRelacao(self, v2)
        if (idRelacao in self.relacoes):
            return self.relacoes[idRelacao]
        return None
