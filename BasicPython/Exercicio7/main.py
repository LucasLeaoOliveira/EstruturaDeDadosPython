lista = []

try:
    lista.append(float(input('Digite o primeiro valor: ')))
    lista.append(float(input('Digite o segundo valor: ')))

    divisao = lista[0]/lista[1]
except ValueError:
    print('Erro! Valor inválido')
except ZeroDivisionError:
    print('Erro!, divisão por zero')
except IndexError:
    print('Erro!, índice inválido')
except KeyboardInterrupt:
    print('Usuário interrompeu a execução')
else:
    print(f"A divisão é {divisao}")

