'''Para revisar o conteúdo prático visto até agora, você agora pode resolver dois exercícios.
 Logo em seguida você pode acessar a aula em vídeo com a solução.
 Implemente cada exercício utilizando tanto o for quanto o while

Ler 5 notas e informar a média
Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)'''
soma = 0

for i in range(1,6):
    nota= float(input("Escreva a nota"))
    soma = soma + nota
print(soma)
media = soma/5
print(media)

soma1 = 0
cont = 0
while cont < 5:
    cont = cont + 1
    nota2 = float(input("Escreva a nota"))
    soma1 = soma1 + nota2
print(soma1)

media2 = soma1/5
print(media2)

for j in range(0,11):
    print(f"3x{j} = ", 3*j)
print()
print("-----------------------------")
print()
cont = 0
while cont <10:
    cont= cont + 1
    print(f"3x{cont} = ", 3*cont)
print()
print("-----------------------------")
print()