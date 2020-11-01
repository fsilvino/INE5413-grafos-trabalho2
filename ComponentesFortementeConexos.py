from BuscaProfundidade import BuscaProfundidade
from GrafoDirigido import GrafoDirigido

class ComponentesFortementeConexos:

    def buscarComponentesFortementeConexos(grafo: GrafoDirigido):
        if type(grafo) is not GrafoDirigido:
            raise Exception("Busca por componentes fortemente conexos funciona apenas com grafos dirigidos.")

        resultBuscaProf = BuscaProfundidade.dfs(grafo) #realiza busca em BuscaProfundidade
        # visitados = resultBuscaProf[0] # C, nas anotacoes da disciplina
        # tempoInicio = resultBuscaProf[1] # T, nas anotacoes da disciplina
        tempoSaida = resultBuscaProf[2] # F, nas anotacoes da disciplina
        # ancestrais = resultBuscaProf[3] # A', nas anotacoes da disciplina

        grafoTransposto = grafo.criarGrafoTransposto()
        ComponentesFortementeConexos.__ordenarVerticesPorTempoSaidaDec(grafoTransposto, tempoSaida)

        resultBuscaProfTransposta = BuscaProfundidade.dfs(grafoTransposto)
        return ComponentesFortementeConexos.__buscarArvoresCompFortConexos(resultBuscaProfTransposta[3])


    def __ordenarVerticesPorTempoSaidaDec(grafoTransposto, tempoSaida):
        verticesComTempo = map(lambda t, v: (t, v), tempoSaida, grafoTransposto.vertices)
        verticesComTempoDesc = sorted(verticesComTempo, key=lambda x: x[0], reverse=True)
        grafoTransposto.vertices = list(map(lambda x: x[1], verticesComTempoDesc))


    def __buscarArvoresCompFortConexos(ancestrais):
        # inverte a lógica da estrutura, gerando um dicionário cuja chave é o "pai" e o valor é o "filho"
        descendentes = dict([(v.numero if v != None else -1, i + 1) for i, v in enumerate(ancestrais)])
        componentes = []
        for i, vertice in enumerate(ancestrais):
            if vertice == None:
                componente = []
                v = i + 1
                componente.append(v)
                while v in descendentes: # se v possui filho, adiciona ele na lista da componente e verifica o filho dele
                    v = descendentes[v]
                    componente.append(v)
                componentes.append(componente)
        return componentes


    def mostrarComponentes(componentes):
        for componente in componentes:
            print(", ".join(map(str, componente)))

            

    buscarComponentesFortementeConexos = staticmethod(buscarComponentesFortementeConexos)
    __ordenarVerticesPorTempoSaidaDec = staticmethod(__ordenarVerticesPorTempoSaidaDec)
    __buscarArvoresCompFortConexos = staticmethod(__buscarArvoresCompFortConexos)
    mostrarComponentes= staticmethod(mostrarComponentes)
