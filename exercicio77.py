from random import randint
soma = []
matriz = []
for i in range(10):
    linha = []
    for j in range(10):
        n = randint(0,99)
        linha.append(n)
    matriz.append(linha)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i + j == len(matriz)-1:
            soma.append(matriz[i][j])
        print(matriz[i][j], end='\t')
    print()
print(sum(soma))