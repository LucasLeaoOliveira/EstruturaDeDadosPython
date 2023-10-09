'''Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
 A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
- Função para ler e retorna o valor da temperatura (não recebe parâmetro)
- Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
- Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão



Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem
 e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com
  a fórmula DISTANCIA = TEMPO * VELOCIDADE.
  Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem,
   com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
   tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
- Função para ler os valores (não recebe parâmetro e retorna os dois valores)
- Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
- Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
- Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)'''

def convert_Fahrenheit2(c):
    F = (9 * c + 160) / 5
    return F

def convert_Fahrenheit():
    c = float(input("Escreva a temperatura em graus Celsius que será convertida para Fahrenheit"))
    F = (9 * c + 160) / 5
    print(F)
def convert_Fahrenheit3(c):
    F = (9 * c + 160) / 5
    print(F)

print(convert_Fahrenheit2(0))

convert_Fahrenheit()

convert_Fahrenheit3(0)

def mostrarVelociadeETempo():
    velocidadeMed = float(input("Escreva a velociade Média do percurso: "))
    tempo = float(input("Escreva o tempo do percurso: "))
    print(f"velocidade média {velocidadeMed}, tempo gasto na viagem{tempo}")

def calculo_da_distancia_da_viagem(velocidadeMed,tempo):
    distancia = velocidadeMed*tempo
    print(f" distância percorrida: {distancia}")

def calculo_de_litros_da_viagem(distancia):
    consumoLitros = distancia/12
    print(f" {consumoLitros}litros foram utilizada na viagem")

def calculo_viagem(velocidadeMed,tempo,distancia,consumoLitros):
    print(f"velocidade média {velocidadeMed},\n tempo gasto na viagem{tempo},\n distância percorrida{distancia}\n {consumoLitros} litros utilizada na viagem")

mostrarVelociadeETempo()
calculo_viagem(10,10,10,10)
calculo_de_litros_da_viagem(10)
calculo_da_distancia_da_viagem(10,10)






