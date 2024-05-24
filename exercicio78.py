''' Preencha uma matriz 6x6 com números aleatórios e multiplique cada elemento da matriz pelo maior 
elemento de sua linha. Escrever a matriz original e a modificada'''

from random import randint

matriz = []
for i in range(6):
    linha = []
    for j in range(6):
        linha.append(randint(0, 9))
    matriz.append(linha)

for i in range(6):
    for j in range(6):
        print(matriz[i][j], end='\t')
    print()

for i in range(6):
    maior = max(matriz[i])
    for j in range(6):
        matriz[i][j] = maior * matriz[i][j]
print()

for i in range(6):
    for j in range(6):
        print(matriz[i][j], end='\t')
    print()