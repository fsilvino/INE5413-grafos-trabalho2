from BuscaProfundidade import BuscaProfundidade
class Conectividade:

    def FortementeConexos(self, grafo):
        if grafo.obterTipoGrafo() != 'Grafo dirigido':
            raise Exception("Busca por compenentes fortemente conexos funciona apenas com grafos dirigidos.")

        result = BuscaProfundidade.dfs(grafo) #realiza busca em BuscaProfundidade
        visitados = result[0] # C, nas anotacoes da disciplina
        tempoInicio = result[1] # T, nas anotacoes da disciplina
        tempoFim = result[2] # F, nas anotacoes da disciplina
        ancestrais = result[3] # A', nas anotacoes da disciplina

        grafoTransposto = grafo.criarGrafoTransposto()
        grafoTransposto = self.ordenaVertices(tempoFim, grafoTransposto)

        result = BuscaProfundidade.dfs(grafoTransposto)

        self.show_result(result[3])
        # chama busca em profundidade para o grafo transposto, fazendo com que a busca seja feita em ordem descrescente do array tempoFim
        # Ou seja, quando maior o valor de tempoFim para o vertice, antes ele eh visitado

    def ordenaVertices(self, tempoFim, grafoTransposto):
        tempoFimDict = {}
        for i in range(0, len(tempoFim)):
            tempoFimDict[i+1] = tempoFim[i]

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


    def show_result(self, lista):
        # para mostrar retorno
        for v in lista:
            if v == None:
                print("None")
            else:
                print(v.numero)

        # algoritmo principal
        i = 1
        raizes = []
        result = []

        for v in lista:
            if v == None:
                raizes.append(i)
            i += 1
        i = 0
        for raiz in raizes:
            result.append([])
            result[i].append(raiz)
            j = 1
            for v in lista:
                if v != None and v.numero == raiz:
                    result[i].append(j)
                j += 1
            i += 1
        print(raizes)
        print(result)
