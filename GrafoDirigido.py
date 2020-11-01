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
        # Verificar se eh necessario adcionar a vertice destino. Sem essa relacao no vertice destino, facilita a organizacao topologica
        self.vertices[v2.numero - 1].adicionarRelacao(relacao)

    def obterTipoGrafo(self):
        return "Grafo dirigido"

    def criarGrafoTransposto(self):
        vertices = self.vertices[:] # para nao ficar na mesma posicao de memoria
        novoGrafo = GrafoDirigido(vertices)

        for v in novoGrafo.vertices:
            v.apagarTodasRelacoes()

        for arco in self.relacoes.values():
            novoGrafo.adicionarRelacao(arco.v2, arco.v1, arco.peso)

        return novoGrafo

    def mostrarGrafo(self):
        print(self.obterTipoGrafo())
        for v in self.vertices:
            saintes = filter(lambda r: r.ehVerticeOrigem(v), v.relacoes.values())
            print(str(v.numero) + ": ", ", ".join(map(lambda r: str(r.obterVerticeDestino(v).numero), saintes)))