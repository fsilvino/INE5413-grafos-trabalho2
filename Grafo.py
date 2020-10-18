from Vertice import Vertice
from Aresta import Aresta
from Arco import Arco

class Grafo:

    def __init__(self):
        self.__reset()
        self.lerArquivo("arquivos-teste/agm_tiny_arco.net")

    def __reset(self):
        self.vertices = []
        self.carregado = False

    def mostrarGrafo(self):
        self.__validarSeFoiCarregado()
        tipoGrafo = "Grafo não direcionado"
        if self.direcionado:
            tipoGrafo = "Grafo direcionado"
        print(tipoGrafo)
        for v in self.vertices:
            print(str(v.numero) + ": " + ", ".join(map(lambda r: str(r.obterOutraParte(v).numero), v.arestas.values())))

    def lerArquivo(self, arquivo):
        self.__reset()
        f = open(arquivo, "r", encoding='utf-8')
        linhas = f.readlines()
        f.close()
        self.__lerVertices(linhas)
        self.__lerRelacoes(linhas)
        self.carregado = True

    def __validarSeFoiCarregado(self):
        if not self.carregado:
            raise Exception("Nenhum arquivo foi carregado! Primeiro carregue um arquivo para poder executar operações no grafo")

    def __lerVertices(self, linhas):
        self.numeroDeVertices = int(linhas[0].split(" ")[1])
        for i in range(1, self.numeroDeVertices + 1):
            linha = linhas[i]
            posicaoEspaco = linha.index(" ")
            numeroVertice = int(linha[0:posicaoEspaco])
            posicaoInicioRotulo = posicaoEspaco + 2
            posicaoFimRotulo = len(linha) - 2
            rotulo = linha[posicaoInicioRotulo:posicaoFimRotulo]
            self.vertices.append(Vertice(numeroVertice, rotulo))


    def __lerRelacoes(self, linhas):
        self.numeroDeRelacoes = 0
        # print(linhas[self.numeroDeVertices + 1])
        for i in range(self.numeroDeVertices + 2, len(linhas)):
            valores = linhas[i].split(" ")

            v1 = self.vertices[int(valores[0]) - 1]
            v2 = self.vertices[int(valores[1]) - 1]
            peso = 1
            if (len(valores) >= 3):
                peso = float(valores[2])

                # visando economizar memória, por ser um grafo não dirigido,
                # criamos uma única vez a representação da relação e adicionamos ela
                # em ambos os vértices

                if linhas[self.numeroDeVertices + 1].strip().lower() == "*edges":
                    self.direcionado = False
                    relacao = Aresta(v1, v2, peso)
                    v2.adicionarRelacao(relacao)
                else:
                    self.direcionado = True
                    relacao = Arco(v1, v2, peso)

                v1.adicionarRelacao(relacao)

                self.numeroDeRelacoes = self.numeroDeRelacoes + 1
