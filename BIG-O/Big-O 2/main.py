# FUNÇÃO 3 DE BIG-O 2
from timeit import timeit

def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista


#print(lista1())
#print("================")
#print(len(lista1()))




tempo_execucao_funcao = timeit(lambda: lista1(), number=10000)

print(f'Tempo de execução (função): {tempo_execucao_funcao} segundos')

#FUNÇAO 4  BIG-O 2

def lista2():
    return range(1000)

l = lista2()

#for i in l:
   # print(i)

tempo_execucao_funcao = timeit(lambda: lista2(), number=10000)

print(f'Tempo de execução (função): {tempo_execucao_funcao} segundos')

