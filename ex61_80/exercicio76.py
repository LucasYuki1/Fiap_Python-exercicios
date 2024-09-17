matriz = []
for i in range(6):
    linha = []
    for j in range(6):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)
for i in range(6):
    print(matriz[i])