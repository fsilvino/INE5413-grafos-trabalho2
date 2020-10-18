# import abc
from abc import ABC,abstractmethod

class Relacao(ABC):

    def __init__(self, verticeOrigem, verticeDestino, peso):
        self.uid = Relacao.gerarIdRelacao(verticeOrigem, verticeDestino)
        self.verticeOrigem = verticeOrigem
        self.verticeDestino = verticeDestino
        self.peso = peso

    def gerarIdRelacao(v1, v2):
        return f'{min(v1.numero, v2.numero)}.{max(v1.numero, v2.numero)}'
    gerarIdRelacao = staticmethod(gerarIdRelacao)

    @abstractmethod
    def obterOutraParte(self, v = None):
        pass
