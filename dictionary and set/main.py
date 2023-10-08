coleta = {'Aedes aegypt': 32, 'Aedes albopictus':22,'Anopheles darlingi':12}

print(coleta['Aedes aegypt'])

print()

print(coleta)

print()

coleta['Rhodnius montenegrensis'] = 11
print()

print(coleta)

print()

del(coleta)['Aedes aegypt']

print()

print(coleta)

print()

print(coleta.items())
print()

print(coleta.keys())

print()

print(coleta.values())

print()

coleta2 = {'Anopheles gambiae':17,'Anopheles deaneorum':22}

print(coleta2)

print()

coleta.update(coleta2)

print(coleta)
print("-------------------------------------------------------------")
for especie, num_especies in coleta.items():
    print(f"Espécie: {especie}, número de espécies: {num_especies} ")
    print("-------------------------------------------------------------")

biomoleculas = ('Proteínas','Ácidos nucleicos','Carboidratos', 'Lipidios',
                'Proteínas','Ácidos nucleicos','Carboidratos', 'Lipidios')

print(biomoleculas)

print()

print(set(biomoleculas))

c1= {1,2,3,4,5}

c2 = {4,5,6,7,8}

c3 = c1.intersection(c2)

print(c3)

print()

print(c1.difference(c2))
print(c2.difference(c1))


