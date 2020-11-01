class BuscaProfundidade:

    def dfs(grafo):
        qtdVertices = grafo.qtdVertices()

        visitados = [False] * qtdVertices
        tempoInicio = [float("inf")] * qtdVertices # marca inicio da visita ao vertice
        tempoFim = [float("inf")] * qtdVertices #marca fim da visita ao vertice
        ancestrais = [None] * qtdVertices

        tempo = 0

        for vertice in grafo.vertices:
            if not visitados[vertice.numero - 1]:
                tempo = BuscaProfundidade.__dfs_visit(vertice, visitados, tempoInicio, tempoFim, ancestrais, tempo)

        return (visitados, tempoInicio, tempoFim, ancestrais)


    def __dfs_visit(vertice, visitados, tempoInicio, tempoFim, ancestrais, tempo):
        posVertice = vertice.numero - 1
        visitados[posVertice] = True # marca vertice como visitados

        tempo += 1
        tempoInicio[posVertice] = tempo # adiciona tempo ao array "tempoInicio", na posicao do vertice
        
        for relacao in vertice.relacoes.values():
            # teste para evitar excecoes onde variavel vertice eh destino da relacao
            if relacao.ehVerticeOrigem(vertice):
                v = relacao.obterVerticeDestino(vertice)
                posV = v.numero -1
                if not visitados[posV]:
                    ancestrais[posV] = vertice # ancestrais recebe variavel "vertice" na posicao onde esta vertice v
                    tempo = BuscaProfundidade.__dfs_visit(v, visitados, tempoInicio, tempoFim, ancestrais, tempo)

        tempo += 1
        tempoFim[posVertice] = tempo # adiciona tempo ao array "tempoFim", na posicao do vertice
        return tempo


    dfs = staticmethod(dfs)
    __dfs_visit = staticmethod(__dfs_visit)
