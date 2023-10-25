

#with open('frase.txt') as text:
    #for linha in text:
        #print(linha)



# Abre o arquivo 'frase.txt' em modo de leitura

with open('frase.txt', 'r') as text:

    # Lê todas as linhas do arquivo e armazena em uma lista

    linhas = text.readlines()

print("__________________________________________")

print(linhas)

print("__________________________________________")


for linha in linhas:
    print(linha.strip())


with open('texto2.txt', 'w') as texto:
    texto.write('olá a todos')

print("__________________________________________")

with open('texto2.txt', 'r') as txt:
    for l in txt:
        print(l)

print("__________________________________________")


