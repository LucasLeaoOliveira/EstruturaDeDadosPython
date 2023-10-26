class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcula_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def mostra_dados(self):
        print('Nome: ', self.nome)
        print('Nota 1:', self.nota1)
        print('Nota 2:', self.nota2)
        print('Média:', self.media)

    def resultado(self):
        if self.media >= 6.0:
            print('Aprovado')
        else:
            print('Reprovado')

aluno2 = Aluno('Osvaldo',1.0,2.0)

aluno = Aluno('Luis',10.0,9.0)

media = aluno.calcula_media()

aluno.mostra_dados()

aluno.resultado()

print("=====================================")

media = aluno2.calcula_media()

aluno2.mostra_dados()

aluno2.resultado()

