from Relacao import Relacao
class Arco(Relacao):

    def obterOutraParte(self):
        return self.verticeDestino
