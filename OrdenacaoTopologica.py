from GrafoDirigido import GrafoDirigido

class OrdenacaoTopologica:

    def ordenar(grafo: GrafoDirigido):
        if type(grafo) is not GrafoDirigido:
            raise Exception("Ordenação topologica funciona apenas com grafos dirigidos.")

        qtdVertices = grafo.qtdVertices()

        visitados = [False] * qtdVertices
        tempoEntrada = [float("inf")]  * qtdVertices
        tempoSaida = [float("inf")]  * qtdVertices

        tempo = 0
        listaOrdenada = [] # nas anotacoes esta apenas como "o"

        for v in grafo.vertices:
            posVertice = v.numero - 1
            if not visitados[posVertice]:
                tempo = OrdenacaoTopologica.__dfs_visit(grafo, v, visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada)

        return listaOrdenada


    def __dfs_visit(grafo, verticeBase, visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada):
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
                    tempo = OrdenacaoTopologica.__dfs_visit(grafo, v, visitados, tempoEntrada, tempoSaida, tempo, listaOrdenada)

        tempo += 1
        tempoSaida[posVerticeOrigem] = tempo # adiciona tempo ao array "tempoFim", na posicao do vertice
        listaOrdenada.insert(0, verticeBase) # insere vertice analisado à esquerda da lista

        # retorna o tempo pois a passagem do parâmetro int na liguagem é por valor e não por referência
        return tempo


    def mostrarOrdenacaoTopologica(lista):
        print(" -> ".join(map(lambda v: v.rotulo, lista)))


    ordenar = staticmethod(ordenar)
    __dfs_visit = staticmethod(__dfs_visit)
    mostrarOrdenacaoTopologica = staticmethod(mostrarOrdenacaoTopologica)
