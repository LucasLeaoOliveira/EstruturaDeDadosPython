import numpy as np

class VetorNaoOrdenado:
    def __init__(self,capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultimaPosicao == -1:
            print( 'O vetor está vazio!!!')

        else:
            for i in range(self.ultimaPosicao + 1):
                print(i,'---', self.valores[i])


if __name__ == '__main__':

    vetor = VetorNaoOrdenado(5)

    vetor.imprime()