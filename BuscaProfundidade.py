class BuscaProfundidade:

    def dfs(self, grafo):
        qtdVertices = GrafoExecutor.qtdVertices(grafo)

        visitados = [False] * qtdVertices
        tempoInicio = [float("inf")] * qtdVertices # marca inicio da visita ao vertice
        tempoFim = [float("inf")] * qtdVertices #marca fim da visita ao vertice
        ancestrias = [None] * qtdVertices

        tempo = 0

        for vertice in grafo.vertices:
            if not visitados[vertice.numero - 1]:
                self.dfs_visit(grafo, vertice, visitados, tempoInicio, tempoFim, ancestrais, tempo)

        return (visitados, tempoInicio, tempoFim, tempo)


    def dfs_visit(self, grafo, vertice, visitados, tempoInicio, tempoFim, ancestrais, tempo):
        posVertice = vertice.numero - 1
        visitados[posVertice] = True # marca vertice como visitados

        tempo += 1
        tempoInicio[posVertice] = tempo# adiciona tempo ao array "tempoInicio", na posicao do vertice
        for v in vertice.arestas.values():
            if not visitados[posVertice]:
                ancestrais[v.numero] = vertice # ancestrais recebe variavel "vertice" na posicao onde esta vertice v
                self.dfs_visit(grafo, vertice, visitados, tempoInicio, tempoFim, ancestrais, tempo)

        tempo += 1
        tempoFim[posVertice] = tempo # adiciona tempo ao array "tempoFim", na posicao do vertice


    dfs = staticmethod(dfs)
