import math

#BIBLIOTECA MATH

print(dir(math))
print(math.sqrt(9))

print(math.sin(45), math.cos(45))

print(math.log(100,10))

print(math.log(2.718281828459045))

print(math.e)

print(math.pi)

#BIBLIOTECA DATETIME
print("--------------------------------------")

import datetime

print(dir(datetime))

print(datetime.date.today())

print(datetime.datetime.now())

data = datetime.date(2023,7,10)

print(data)

print(data.day)

print(data.month)

print(data.year)

horario = datetime.datetime(2023,10,10,7,30,0)

print(horario)

#BIBLIOTECA RANDOM
print("--------------------------------------")

import random

print(random.random())

print(random.randint(1,10))

print(random.randrange(0,10,2))

print(random.randrange(0,10,3))

x = ['k','d',13,'34-j','x']

print(random.choice(x))

#BIBLIOTECA time
print("--------------------------------------")

import time as tm

print(tm.time())

antes = tm.time()

lista = []

for i in range(0,100000):
    lista.append(i)
depois = tm.time()

intervalo = depois - antes

print(f"tempo : {intervalo} segundo")


print("FINALIZANDO...")

tm.sleep(1)
print("5")

tm.sleep(1)
print("4")
tm.sleep(1)
print("3")
tm.sleep(1)
print("2")
tm.sleep(1)
print("1")
tm.sleep(1)
print("até a próxima!!")

