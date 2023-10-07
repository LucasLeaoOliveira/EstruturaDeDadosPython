'''(1)Leia a idade do usuário e classifique-o em:
    - Criança – 0 a 12 anos
    - Adolescente – 13 a 17 anos
    - Adulto – acima de 18 anos
    -Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida'''
'''idade = int(input("Escreva sua idade: "))

if idade <=12 and idade>=0:
    print("Você É UMA CRIANÇA ")
elif 13 <= idade and idade<= 17:
    print("Voc ê É UMA Adolescente ")
elif idade>17:
    print("Você É UMA Adulto ")
else:
    print("idade é inválida")'''

'''Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; 
passando por um cálculo da média aritmética. 
Após a média calculada, devemos anunciar se o aluno foi aprovado,
 reprovado ou pegou exame
- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
- Se a média for maior do que 6.0, o aluno está aprovado
- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado'''

'''m1 = float(input("Escreva a nota 1:"))
m2 = float(input("Escreva a nota 2:"))
m3 = float(input("Escreva a nota 3:"))
if m1 < 0 or m2 < 0 or m3 < 0:
    print("valor invalido")
else:
    media = (m1 + m2 + m3) / (3)

    if 0.0 <= media <= 4.0:
        print("reprovado")
    elif 4.1 <= media <= 6.0:
        print('pegou exame')
        x = float(input("Qual foi a nota do exame?: "))
        if x >= 6.0:
            print("está aprovado")
        else:
            print("está reprovado")
    else:
        print("aprovado")'''
