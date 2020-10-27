class OrdenacaoTopologica:

    def ordenar(self, grafo):
        if grafo.obterTipoGrafo != 'Grafo dirigido':
            raise Exception("Ordenação topologica funciona apenas com grafos dirigidos.")

        qtdVertices = grafo.qtdVertices()

        visitados = [False] * qtdVertices
        tempoEntrada = [float("inf")]  * qtdVertices
        tempoSaida = [float("inf")]  * qtdVertices

        tempo = 0
        listaOrdenada = [] # nas anotacoes esta apenas como "o"

        for v in grafo.vertices:
            posVertice = v.numero -1
            if not visitados[posVertice]:
                visitados[posVertice] = True
                result = self.dfs_visit(grafo, v, visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada)
                visitados = result[0]
                tempoEntrada = result[1]
                tempoSaida = result[2]
                tempo = result[3]
                listaOrdenada = result[4]

        return listaOrdenada
        # self.show_result(listaOrdenada)

    def dfs_visit(self, grafo, verticeOrigem, visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada):
        posVerticeOrigem = verticeOrigem.numero - 1
        visitados[posVerticeOrigem] = True
        tempo += 1
        tempoEntrada[posVerticeOrigem] = tempo
        # for v in grafo.vertices.arestas.values():
        for v in grafo.vertices:
            posVertice = v.numero - 1
            if not visitados[posVertice]:
                result = self.dfs_visit(grafo, v, visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada)
                visitados = result[0]
                tempoEntrada = result[1]
                tempoSaida = result[2]
                tempo = result[3]
                listaOrdenada = result[4]

        tempo += 1
        tempoSaida[posVerticeOrigem] = tempo # adiciona tempo ao array "tempoFim", na posicao do vertice
        listaOrdenada.insert(0, verticeOrigem) # insere vertice analisado à esquerda da lista
        return (visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada)

    def show_result(self, lista):
        i = 0
        for v in lista:
            i += 1
            print(str(i)+":" + v.rotulo)
