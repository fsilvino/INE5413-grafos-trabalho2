from BuscaProfundidade import BuscaProfundidade
class ComponentesFortementeConexos:

    def buscarComponentesFortementeConexos(self, grafo):
        if grafo.obterTipoGrafo() != 'Grafo dirigido':
            raise Exception("Busca por componentes fortemente conexos funciona apenas com grafos dirigidos.")

        resultBuscaProf = BuscaProfundidade.dfs(grafo) #realiza busca em BuscaProfundidade
        # visitados = resultBuscaProf[0] # C, nas anotacoes da disciplina
        # tempoInicio = resultBuscaProf[1] # T, nas anotacoes da disciplina
        tempoSaida = resultBuscaProf[2] # F, nas anotacoes da disciplina
        # ancestrais = resultBuscaProf[3] # A', nas anotacoes da disciplina

        grafoTransposto = grafo.criarGrafoTransposto()
        grafoTransposto = self.ordenarVerticesPorTempoSaidaDec(grafoTransposto, tempoSaida)

        resultBuscaProfTransposta = BuscaProfundidade.dfs(grafoTransposto)
        return resultBuscaProfTransposta[3]

    def ordenarVerticesPorTempoSaidaDec(self, grafoTransposto, tempoSaida):
        tempoFimDict = {}
        for i in range(0, len(tempoSaida)):
            tempoFimDict[i+1] = tempoSaida[i]

        listaChavesOrdenadas = sorted(tempoFimDict, key= lambda d: tempoFimDict[d], reverse=True)

        tempoFimDictOrdenado = {}
        for key in listaChavesOrdenadas:
            tempoFimDictOrdenado[key] = tempoFimDict[key]
        numVertOrdenados = list(tempoFimDictOrdenado)

        verticesOrdenados = []
        for i in numVertOrdenados:
            verticesOrdenados.append(grafoTransposto.vertices[i-1])

        grafoTransposto.vertices = verticesOrdenados
        return grafoTransposto


    def buscarProximoVertice(self, ancestrais, arvores, raiz, posicaoArvore):
        for i, vertice in enumerate(ancestrais):
            if vertice != None and vertice.numero == raiz:
                arvores[posicaoArvore].append(i+1)
                self.buscarProximoVertice(ancestrais, arvores, i+1, posicaoArvore)
        return arvores

    def buscarArvoresCompFortConexos(self, ancestrais):
        raizes = []
        arvores = []
        for i, vertice in enumerate(ancestrais):
            if vertice == None:
                raizes.append(i+1)

        for i, raiz in enumerate(raizes):
            arvores.append([raiz])
            arvores = self.buscarProximoVertice(ancestrais, arvores, raiz, i)
        return arvores

    def show_result(self, arvores):
        for arvore in arvores:
            print(", ".join(map(str, arvore ) ) )
