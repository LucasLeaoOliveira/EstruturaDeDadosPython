texto = "Minha casa fica na rua Carneiro, 78. O CEP é 88388-000 e 11111-111 meu site é https://www.iaexpert.academy http://iaexpert.com.br"

import re

print(re.findall('\d',texto))
print()
#print(re.findall('\D',texto)) --> todos que não são números

#print(re.findall('\W',texto)) --> todos que não são letras

print(re.findall('\d{5}-\d{3}',texto))

print()

print(re.findall('https?://[A-Za-z0-9./]+', texto))