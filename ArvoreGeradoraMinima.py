class ArvoreGeradoraMinima:

    # utilizando algoritmo de kruskal
    def montarArvoreGeradoraMinima(self, grafo):
        # print("Chegou aqui")
        a = []
        s = [None] * grafo.qtdVertices()
        # colocando apenas numeros dos vertices para facilitar comparacoes
        for v in grafo.vertices:
            s[v.numero - 1] = [v.numero]

        #traz arestas ordenadas por peso
        arestas = self.ordenarArestas(grafo.relacoes)
        for aresta in arestas.values():
            # aresta = arestas[key]
            verticeOrigem = aresta.v1
            verticeDestino = aresta.obterVerticeDestino(verticeOrigem)

            # guarda posicoes em array, para facilitar busca na estrtura s
            posOrigem =verticeOrigem.numero -1
            posDestino = verticeDestino.numero -1

            if s[posOrigem] != s[posDestino]:
                a.append(aresta) # adiciona aresta a lista de arestas da agm

                novoConj = s[posOrigem] + s[posDestino]
                # ordenacao para coparacao de arrays, pois os "==" compara elemento por elemento
                novoConj.sort()

                for x in s[posOrigem]:
                    s[x -1] = novoConj

                for x in s[posDestino]:
                    s[x -1] = novoConj

        return a
        self.show_result(a)

    def ordenarArestas(self, relacoes):
        arestasOrdenadas = {}

        #retorna lista ordenada das CHAVES do dicionario de relacoes, de acordo com o peso da relacao guardada naquela chave do dicionario
        listaChavesOrdenadas = sorted(relacoes, key= lambda r: relacoes[r].peso)

        for key in listaChavesOrdenadas:
            arestasOrdenadas[key] = relacoes[key]

        return arestasOrdenadas


    def show_result(self, lista):
        soma = 0
        for a in lista:
            soma += a.peso
        print(soma)
        print(", ".join(map(lambda a : str(a.v1.numero)+"-"+str(a.v2.numero), lista ) ) )
        # for a in lista:
            # print(str(s[posOrigem]) + " : " + str(a.v2.numero) + ", Peso: "+ str(a.peso))
