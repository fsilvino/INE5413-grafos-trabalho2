from Relacao import Relacao
class Arco(Relacao):

    def obterOutraParte(self, v =None):
        return self.verticeDestino
