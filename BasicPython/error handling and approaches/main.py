try:
    # Código que pode causar um erro
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("O resultado é:", resultado)


except Exception as e:
    # Captura qualquer outra exceção não tratada
    print("Erro desconhecido:", e)


# ERRO DE SYNTAX 3 = 4

#ERRO de varialvel não definida ===> print("meu nome é:",nome)

#ERRO de divisão por 0

#ERRO de Type 2.8/"cachorro"

#ERRO index c = [1,2,3,4,5]  c[7]

while True:
    try:
        n = int(input("Digite um numero inteiro: "))
        # n = diqwdqwdqw  daria ValueError
    except Exception as e:
         print("Erro desconhecido:", e)
    else:
        print(f"Valor digitado é:{n}")
        break

while True:
    try:
        p = int(input("digite um numero inteiro: "))
    except ValueError:
        print("Valor inválido")
    except KeyboardInterrupt:
        print("Usuario interrompeu a execução")
        break
    else:
        print(f"Valor digitado é: {p}")
        break