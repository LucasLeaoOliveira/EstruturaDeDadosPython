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

    def insere(self,valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print('Capacidade máxima atingida!!!')
        else:
            self.ultimaPosicao +=1
            self.valores[self.ultimaPosicao] = valor

    def pesquisar(self,valor):
            for i in range(self.ultimaPosicao + 1):
                if valor == self.valores[i]:
                    print(i)
            return -1

if __name__ == '__main__':

    vetor = VetorNaoOrdenado(5)

    vetor.imprime()
    print('===========')
    vetor.insere(1)
    print('===========')
    vetor.imprime()
    print('===========')
    vetor.insere(2)
    print('===========')
    vetor.imprime()
    print('===========')
    vetor.insere(3)
    print('===========')
    vetor.imprime()
    print('===========')
    vetor.insere(4)
    print('===========')
    vetor.imprime()
    print('===========')
    vetor.insere(5)
    print('===========')
    vetor.imprime()
    print('===========')
    vetor.insere(6)
    print('============')
    print(vetor.ultimaPosicao)
    print('============')
    print(vetor.valores)
    print('============')
    vetor.pesquisar(4)
    print('============')
    vetor.pesquisar(50)
