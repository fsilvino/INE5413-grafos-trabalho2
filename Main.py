from Grafo import Grafo

g = Grafo()

def solicitarOpcao(texto, min, max, maxTentativas = 3):
    tentativas = 1
    while tentativas <= maxTentativas:
        try:
            opcao = int(input(texto))
            if opcao >= min and opcao <= max:
                return opcao
            else:
                raise Exception()
        except:
            print("Opção inválida. Digite um valor entre " + str(min) + " e " + str(max))

        tentativas += 1

    return min - 1

def solicitarVertice(texto="Digite o número do vertice: "):
    try:
        v = solicitarOpcao(texto, 1, g.qtdVertices())
        if v > 0:
            return v
        else:
            print("Você não digitou um vértice válido")
    except Exception as ex:
        print(ex)
        return 0

def carregarArquivo():
    arquivoPadrao = "grafo.teste.net"
    arquivo = input("Digite o nome do arquivo (em branco carrega " + arquivoPadrao + "): ")
    try:
        if arquivo == "":
            arquivo = arquivoPadrao

        g.lerArquivo(arquivo)
        print("Arquivo " + arquivo + " carregado com sucesso.")
    except Exception as ex:
        print("Não foi possível ler o arquivo!")
        print(ex)

def mostrarGrafo():
    try:
        print('Mostrando o grafo:')
        g.mostrarGrafo()
    except Exception as ex:
        print(ex)


# lista com funcoes que serao executadas
acoes = [
    {"texto": "Carregar um arquivo", "funcao": carregarArquivo},
    {"texto": "Mostrar o grafo", "funcao": mostrarGrafo},
]

user_input = -1
while user_input != 0:
    print()
    print("Menu: ")
    for i, acao in enumerate(acoes):
        print(str(i + 1) +" - " + acao["texto"])
    print("0 - Finalizar o programa")
    print()

    user_input = solicitarOpcao("Digite a opção desejada: ", 0, len(acoes))
    print()
    if user_input > 0:
        acoes[user_input - 1]["funcao"]()
        print()
        input('Pressione ENTER para continuar...')
    else:
        user_input = 0

# fim while
print()
print("Programa finalizado")
