import numpy as np


class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultimaPosicao == -1:
            print('O vetor está vazio!!!')

        else:
            for i in range(self.ultimaPosicao + 1):
                print(i, '---', self.valores[i])

    def insere(self, valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print('Capacidade máxima atingida!!!')
        else:
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)

        if posicao == -1:
            print(f'Não há termo {valor} para excluir')
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]

            self.ultimaPosicao -= 1
            print(f'Termo {valor} excluído com sucesso')


if __name__ == '__main__':
    vetor = VetorNaoOrdenado(8)

    vetor.imprime()
    vetor.insere(1)
    vetor.insere(2)
    vetor.insere(3)
    vetor.insere(4)
    vetor.insere(5)
    vetor.insere(6)
    vetor.insere(69)
    vetor.imprime()
    print("-----------------------")
    vetor.excluir(-1)
    print("-----------------------")
    vetor.excluir(69)
    print("-----------------------")
    vetor.imprime()

    vetor1 = VetorNaoOrdenado(10)

    vetor1.excluir(1)

    print("---------------------------")

    vetor1.imprime()

    print('------------------------------')

    vetor1.insere(1)
    vetor1.insere(5)
    vetor1.insere(6)
    vetor1.insere(2)
    vetor1.insere(22)
    vetor1.insere(10)

    vetor1.imprime()

    print()

    vetor1.excluir(22)

    vetor1.imprime()