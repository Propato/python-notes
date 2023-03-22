print('Matriz como lista de listas:')

matriz = [[1, 0, 0], [0, 1, 1], [0, 0, 1]]

print(matriz)

# cada linha da matriz é uma lista
for linha in matriz:
    # cada valor é uma posição da lista
    for valor in linha:
        print(valor, end=" ")

    print()

# biblioteca numpy

print('Matriz com numpy:')
import numpy as np

# cria matriz
matriz = np.array([[1, 0, 0],
                  [0, 1, 1],
                  [0, 0, 1]], 
                  dtype=int)

print(matriz)
for i in range(3):
    # cada valor é uma posição da lista
    for j in range(3):
        print(matriz[i][j], end=" ")

    print()

# recebe dimensões e cria matriz preenchida com zeros
matriz = np.zeros((2, 3), dtype=int)
print('Matriz de zeros:\n', matriz)

matriz = np.ones((2, 3), dtype=int)
print('Matriz de uns:\n', matriz)

# com numpy os operadores são sobrescritos, ou seja, podemos usar -, +, /, * para aplicar na matriz inteira, sem precisar rodar valor por valor