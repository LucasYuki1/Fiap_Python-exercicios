matriz = []
for i in range(5):          # quantidade de linhas
    linha = []
    for j in range(4):      # quantidade de colunas
        n = int(input('Numero: '))
        linha.append(n)
    matriz.append(linha)

# exibe a matriz
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end='\t')
    print()
search = int(input("Digite um número pra fazer a busca: "))
num = []

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if search == matriz[i][j]:
            print(f'O índice do número é: {(i+1),(j+1)}')
                