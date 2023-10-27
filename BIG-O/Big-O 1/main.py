

#FUNÇÃO 0(n)
from timeit import timeit


def soma1(n):
    soma = 0
    for i in range(n+1):
        soma +=i
    return soma

print(soma1(10))

# Medindo o tempo de execução usando uma string com stmt
tempo_execucao_string = timeit('soma1(10)', globals=globals(), number=100000)
print(f'Tempo de execução (string): {tempo_execucao_string} segundos')

# Medindo o tempo de execução usando uma função com stmt
tempo_execucao_funcao = timeit(lambda: soma1(10), number=100000)
print(f'Tempo de execução (função): {tempo_execucao_funcao} segundos')

def soma2(n):
    return (n*(n+1))/2

tempo_execucao_string1 = timeit('soma2(10)', globals=globals(), number=100000)
print(f'Tempo de execução (string): {tempo_execucao_string1} segundos')

tempo_execucao_funcao2 = timeit(lambda: soma2(10), number=100000)
print(f'Tempo de execução (função): {tempo_execucao_funcao2} segundos')

