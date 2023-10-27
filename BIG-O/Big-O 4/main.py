# constant O(1)

lista = [1, 2, 3, 4, 5]


def constant(n):
    print(n[0])


constant(lista)

print("--------------------------")


# constant LINEAR O(n)

def linear(n):
    for i in n:
        print(i)


linear(lista)

print("-----------------------------")


# Quadratic - O(n^2) - polynomial

def quadratic(n):
    for i in n:
        for j in n:
            print(i, j)
        print("-----")
quadratic(lista)

print("-----------------------------")


#COMBINATION



# O(1) + O(5) + O(n) + O(n) + O(3)

# O(9) + 2 O(n) ---->  O(n)

def combination(n):

    # O(1)

    print(n[0])

    #O(5)

    for i in range(5):
        print('test', i)

    #O(n)

    for i in n:
        print(i)

    # O(n)

    for i in n:
        print(i)

    #O(3)

    print('Python')
    print('Python')
    print('Python')

combination(lista)