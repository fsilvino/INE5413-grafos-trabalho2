from BuscaProfundidade import BuscaProfundidade
class Conectividade:

    def FortementeConexos(self, grafo):
        (visitados, tempoInicio, tempoFim, tempo) = BuscaProfundidade.dfs(grafo) #realiza busca em BuscaProfundidade

        #cria grafo transposta (todas as direcoes trocadas)

        # chama busca em profundidade para o grafo transposto, fazendo com que a busca seja feita em ordem descrescente do array tempoFim
        # Ou seja, quando maior o valor de tempoFim para o vertice, antes ele eh visitado
