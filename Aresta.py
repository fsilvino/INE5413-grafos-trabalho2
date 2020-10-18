from Relacao import Relacao
class Aresta(Relacao):



    def obterOutraParte(self, v):
        return self.v1 if self.v1.numero != v.numero else self.v2

    
