import re

#FUNÇÃO SEARCH

frase = 'Olá, meu número de telefone é (42)00010-0000'

print(frase)
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase))

print("===========================================")

placaCarro = 'A placa do carro que eu anotei durante o acidente foi FrT-1998'
print(placaCarro)
print(re.search('[A-Za-z]{3}-\d{4}',placaCarro))

print("===========================================")

email = 'Entre em contato, meu email é luk@gmail.com'

print(re.search('\w+@\w+\.com',email))



#FUNÇÃO MATCH


frase2 = 'FrT-1998 é a placa do carro'

print()
print("=================================================================")

print(re.match('[A-Za-z]{3}-\d{4}',placaCarro))

print(re.match('[A-Za-z]{3}-\d{4}',frase2))

print()
print("=================================================================")


#FUNÇÃO FINDALL

frase3 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'

print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase3))

emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''


print(re.findall('\w+@\w+\.\w*',emails))