class OrdenacaoTopologica:

    def ordenar(self, grafo):
        if grafo.obterTipoGrafo() != 'Grafo dirigido':
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
                # essa parte abaixo eh omitida nas anotacoes da disciplica, mas eh necessaria para o algoritmo funcionar
                visitados = result[0]
                tempoEntrada = result[1]
                tempoSaida = result[2]
                tempo = result[3]
                listaOrdenada = result[4]

        return listaOrdenada
        # self.show_result(listaOrdenada)

    def dfs_visit(self, grafo, verticeBase, visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada):
        posVerticeOrigem = verticeBase.numero - 1
        visitados[posVerticeOrigem] = True
        tempo += 1
        tempoEntrada[posVerticeOrigem] = tempo

        for key in verticeBase.relacoes:
            # teste para evitar excecoes onde variavel verticeBase eh destino da relacao
            if verticeBase.relacoes[key].ehVerticeOrigem(verticeBase):
                v = verticeBase.relacoes[key].obterVerticeDestino(verticeBase)
                posVertice = v.numero - 1
                if not visitados[posVertice]:
                    result = self.dfs_visit(grafo, v, visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada)
                    # essa parte abaixo eh omitida nas anotacoes da disciplica, mas eh necessaria para o algoritmo funcionar
                    visitados = result[0]
                    tempoEntrada = result[1]
                    tempoSaida = result[2]
                    tempo = result[3]
                    listaOrdenada = result[4]

        tempo += 1
        tempoSaida[posVerticeOrigem] = tempo # adiciona tempo ao array "tempoFim", na posicao do vertice
        listaOrdenada.insert(0, verticeBase) # insere vertice analisado à esquerda da lista
        # essa retorno eh omitido nas anotacoes da disciplica, mas eh necessaria para o algoritmo funcionar
        return (visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada)

    def show_result(self, lista):
        i = 0
        for v in lista:
            i += 1
            print(str(i)+":" + v.rotulo)
