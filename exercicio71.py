matriz = []
for i in range(3):          # quantidade de linhas
    linha = []
    for j in range(5):      # quantidade de colunas
        n = int(input('Numero: '))
        linha.append(n)
    matriz.append(linha)

# exibe a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()
