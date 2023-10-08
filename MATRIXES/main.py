import numpy as np

matriz = np.array([[2,3,1],[4,5,7]])
print("-----------------------")
print(matriz)
print("-----------------------")
print(matriz.shape)
print("-----------------------")

print(matriz[0])
print("-----------------------")
print(matriz[1])
print("-----------------------")
print(matriz[0][1])
print("-----------------------")
print(matriz[1][1])
print("-----------------------")

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])
