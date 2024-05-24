matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        n = int(input('digite: '))
        linha.append(n)
    matriz.append(linha)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()
    