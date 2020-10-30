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

        lista = self.buscaArvores(result[3])
        self.show_result(lista)
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


    def x(self, lista, result, raiz, posicao):
        for i, x in enumerate(lista):
            if x != None and x.numero == raiz:
                result[posicao].append(i+1)
                self.x(lista, result, i+1, posicao)
        return result

    def buscaArvores(self, lista):
        raizes = []
        result = []
        for i, v in enumerate(lista):
            if v == None:
                raizes.append(i+1)

        for i, raiz in enumerate(raizes):
            result.append([raiz])
            result= self.x(lista, result, raiz, i)
        return result

    def show_result(self, lista):
        for arvore in lista:
            print(", ".join(map(str, arvore ) ) )
