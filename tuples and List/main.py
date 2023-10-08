tupla = ('Homo sapiens','Canis familiaris','Felis catus')
print(tupla[0])
print(tupla[1])
print(tupla[2])

print(tupla.index('Canis familiaris'))

for i in tupla:
    print(i)

list1 = ['Homo sapiens','Canis familiaris','Felis catus']

list2 = ['Lucas Leão', 'Heloisa']

print(list1,'\n',list2)

lista3 = list1 + list2

print(lista3)

lista2_nova = list2*2
print(lista2_nova)

print(list2[0],"\n",list2[1])

print(list1[0:2])

list2.append('Amor')

print(list2)

list2.remove('Amor')

print(list2)

for j in list1:
    print(j)