def mensagem():
    print("Hello word")

mensagem()

def mensagem(texto):
    print(texto)

mensagem("lucas")

#mensagem() mensagem() missing 1 required positional argument: 'texto'

mensagem('gg')
mensagem('12321312321312')


def soma(a,b):
    soma = a+b
    print(soma)

soma(2,3)


def soma(a,b):
    return a + b

r = soma(2,3)

print(r)

def calcula_energia_potencia_gravitacional(m,h,g=9.8):
    energia = g*m*h
    return energia

print(calcula_energia_potencia_gravitacional(10,10))


