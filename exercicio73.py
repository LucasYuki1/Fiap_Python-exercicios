from random import randint

matriz = []
for i in range(5):          # quantidade de linhas
    linha = []
    for j in range(5):      # quantidade de colunas
        n = randint(0,99)
        linha.append(n)
    matriz.append(linha)
c = []
# exibe a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            c.append(matriz[i][j])
        #diagonal invertida
        #if i + j == len(matriz)-1
        print(matriz[i][j], end='\t')
    print()
print(sum(c))