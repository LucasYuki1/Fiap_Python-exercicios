from random import randint
minimo = []
matriz = []
for i in range(5):          # quantidade de linhas
    linha = []
    for j in range(4):      # quantidade de colunas
        n = randint(0,99)
        linha.append(n)
        minimo.append(n)
    matriz.append(linha)

# exibe a matriz
#menor = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        #if matriz[i][j] < menor:
            #menor = matriz[i][j]
        #print(menor)
        print(matriz[i][j], end='\t')
    print()
print(min(minimo))