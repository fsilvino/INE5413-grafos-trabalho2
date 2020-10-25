from Grafo import Grafo
from Arco import Arco

class GrafoDirigido(Grafo):

    def gerarIdRelacao(self, v1, v2):
        return f'{v1.numero}.{v2.numero}'

    def adicionarRelacao(self, v1, v2, peso):
        id = self.gerarIdRelacao(v1, v2)
        relacao = Arco(id, v1, v2, peso)
        self.relacoes[id] = relacao
        self.vertices[v1.numero - 1].adicionarRelacao(relacao)
        self.vertices[v2.numero - 1].adicionarRelacao(relacao)

    def obterTipoGrafo(self):
        return "Grafo dirigido"
