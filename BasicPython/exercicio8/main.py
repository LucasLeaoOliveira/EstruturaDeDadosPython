# Dicionário com o nome dos alunos e suas respectivas notas
alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

# Gravando os alunos no arquivo de texto
with open('alunos_notas.txt', 'w') as arquivo:
    for nome, nota in alunos.items():
        # Escreve cada aluno em uma nova linha no arquivo
        arquivo.write(f"{nome},{nota}\n")

# Lendo e mostrando os alunos do arquivo de texto
with open('alunos_notas.txt', 'r') as arquivo:
    for linha in arquivo:
        # Divide a linha em nome e nota usando a vírgula como delimitador
        nome, nota = linha.strip().split(',')
        # Mostra o aluno
        print(f"Aluno: {nome}, Nota: {nota}")
