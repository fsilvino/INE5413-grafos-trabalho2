class ArvoreGeradoraMinima:

    # utilizando algoritmo de kruskal
    def montarArvoreGeradoraMinima(grafo):
        # print("Chegou aqui")
        a = []
        s = [None] * grafo.qtdVertices()
        # colocando apenas numeros dos vertices para facilitar comparacoes
        for v in grafo.vertices:
            s[v.numero - 1] = [v.numero]

        #traz arestas ordenadas por peso
        arestas = sorted(grafo.relacoes.values(), key=lambda r: r.peso)
        for aresta in arestas:
            # aresta = arestas[key]
            verticeOrigem = aresta.v1
            verticeDestino = aresta.obterVerticeDestino(verticeOrigem)

            # guarda posicoes em array, para facilitar busca na estrtura s
            posOrigem = verticeOrigem.numero - 1
            posDestino = verticeDestino.numero - 1

            if s[posOrigem] != s[posDestino]:
                a.append(aresta) # adiciona aresta a lista de arestas da agm

                novoConj = s[posOrigem] + s[posDestino]
                # ordenacao para coparacao de arrays, pois o "!=" do if acima compara elemento por elemento
                novoConj.sort()

                for x in novoConj:
                    s[x -1] = novoConj

        return a
    montarArvoreGeradoraMinima = staticmethod(montarArvoreGeradoraMinima)

    def mostrarAGM(lista):
        print(sum(map(lambda a: a.peso, lista)))
        print(", ".join(map(lambda a : str(a.v1.numero) + "-" + str(a.v2.numero), lista)))
    mostrarAGM = staticmethod(mostrarAGM)
