#Manipulation Strings

a = 'casaco'
print("==============================")
print()
print(a)
print()
print("==============================")
print()
maiuscula = a.upper()
print(a,maiuscula)
print()
print("==============================")
print()
minuscula = maiuscula.lower()
print(maiuscula,minuscula)
print()
print("==============================")
print()
capital = a.capitalize()
print(capital)
print()
print("==============================")
print()
metade_palavra = a[0:4]
print(metade_palavra)
print()
print("==============================")
print()
ultimas_letras = a[3:]
print(ultimas_letras)
print()
print("==============================")
print()
b = a.replace('aco','inha')
print(a)
print(b)
print()
print("==============================")
print()
c = a.replace('o','a')
print(c)
print()
print("==============================")
print()
print(c.find('s'))
print()
print("==============================")
print()
print(c.find('b'))  #" a função find só dá -1 como resposta, se ela não achar  o 'char' que voce deseja"
print()
print("==============================")
print()
e = ' casaco '
print(len(e))
print()
print("==============================")
print()
f = e.strip()
print(f)
print()
print(len(f))
print()
print("==============================")
print()
n1 = 14
n2 = 16
print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')
print()