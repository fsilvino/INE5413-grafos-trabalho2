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
                result = BuscaProfundidade.dfs_visit(vertice, visitados, tempoInicio, tempoFim, ancestrais, tempo)
                visitados = result[0]
                tempoEntrada = result[1]
                tempoSaida = result[2]
                tempo = result[3]
                ancestrais = result[4]

        return (visitados, tempoInicio, tempoFim, ancestrais)


    def dfs_visit(vertice, visitados, tempoInicio, tempoFim, ancestrais, tempo):
        posVertice = vertice.numero - 1
        visitados[posVertice] = True # marca vertice como visitados

        tempo += 1
        tempoInicio[posVertice] = tempo# adiciona tempo ao array "tempoInicio", na posicao do vertice
        for key in vertice.relacoes:
            # teste para evitar excecoes onde variavel vertice eh destino da relacao
            if vertice.relacoes[key].ehVerticeOrigem(vertice):
                v = vertice.relacoes[key].obterVerticeDestino(vertice)
                posV = v.numero -1
                if not visitados[posV]:
                    ancestrais[posV] = vertice # ancestrais recebe variavel "vertice" na posicao onde esta vertice v
                    result = BuscaProfundidade.dfs_visit(v, visitados, tempoInicio, tempoFim, ancestrais, tempo)
                    visitados = result[0]
                    tempoInicio = result[1]
                    tempoFim = result[2]
                    tempo = result[3]
                    ancestrais = result[4]

        tempo += 1
        tempoFim[posVertice] = tempo # adiciona tempo ao array "tempoFim", na posicao do vertice
        return (visitados, tempoInicio, tempoFim, tempo, ancestrais)


    dfs = staticmethod(dfs)
    dfs_visit = staticmethod(dfs_visit)
