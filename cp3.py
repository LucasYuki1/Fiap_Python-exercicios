# Integrantes do grupo:
# Alice Santos Bulhões - RM: 554499
# Lucas Henzo Ide Yuki - RM: 554865

matriz_usuario = 0

# Função do menu do usuário, mostra as opções e retorna um valor pra determinar
# qual função será acionada a partir do valor fornecido pelo usuário


def menu():
    print("""
    1-Verificar se o número é perfeito
    2-Verificar se lista é palíndromo
    3-Preencher matriz
    4-Exibir matriz
    5-Somar elementos acima da diagonal principal
    6-Finalizar
    """)
    escolha = int(input('Selecione sua opção: ')
                  )   # Input de escolha do usuário
    return escolha                                  # Retorna o valor informado


# Função da verificação de um número perfeito
def perfeito(numPerfeito):
    somaPerfeito = 0                        # Determina uma variável que armazena soma
    for i in range(1, numPerfeito):
        if numPerfeito % i == 0:            # Caso o módulo do número fornecido pela variável i for igual a 0
            # A variável de soma receberá o número i que é um divisor do número inserido
            somaPerfeito += i
    if somaPerfeito == numPerfeito:
        print("É um número perfeito")       # Mostra no terminal
    else:
        print("Não é um número perfeito")


# Função de identifficação de uma lista palíndromo
def palindromo(lista):                  # Recebe os valores recebidos pelo usuário
    # Cria uma nova variável que é a lista com índices negativos
    lista1 = lista[::-1]
    if lista1 == lista:                 # Faz a verificação  do inverso da lista se é igual a lista em ordem normal
        print('É um palíndromo')        # Mostra no terminal
    else:
        print('Não é um palindromo')


# Função que preenche a matriz com valores fornecidos pelo usuário
# Recebe os parâmetros fornecidos pelo usuário
def preencher_matriz(linha, coluna):
    matriz = []                                     # Cria a variável da matriz
    for i in range(linha):                          # Recebe a quantidade de linhas
        linha = []
        for j in range(coluna):                     # Recebe a quantidade de colunas
            # Solicita um número ao usuário
            n = int(input('Digite um número: '))
            # Adiciona na linha um valor
            linha.append(n)
        # Adiciona a lista de linhas na matriz
        matriz.append(linha)
    print('Matriz armazenada com sucesso!')
    return matriz                                   # Retorna a matriz


# Função que exibe a matriz
def exibir_matriz(matriz):
    # Percorre a matriz e exibe os valores no terminal
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()


# Função de somar elementos acima da diagonal principal
def somar_diagonal(matriz):
    # Determina uma váriavel que receberá os valores da matriz
    somaNum = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i < j:                       # Se o valor da linha for menor do que o valor da coluna
                # A variável receberá os valores dos elementos acima da diagonal principal
                somaNum += matriz[i][j]
    return somaNum                          # Retorna a soma dos elementos


# Começo do programa
escolha = menu()

while escolha != 6:
    if escolha == 1:
        # Chama a função e recebe um parametro
        perfeito(int(input('Digite um número: ')))
    elif escolha == 2:
        lista = []
        # Preenche uma lista com a quantidade de números que o usuário informar
        for i in range(1, int(input('Quantos números da lista você deseja colocar? '))+1):
            # Recebe os valores e informa os parâmetros da função palindromo
            n = int(input('Digite um número: '))
            lista.append(n)
        # Chama a função e recebe um parâmetro
        palindromo(lista)
    elif escolha == 3:
        # Usuário informa a quantidade de linhas dentro da matriz
        linha = int(input('Quantidade de linhas: '))
        # Usuário informa a quantidade de colunas
        coluna = int(input('Quantidade de colunas: '))
        # Chama a função e recebe um parâmetro
        matriz_usuario = preencher_matriz(linha, coluna)
    elif escolha == 4:
        # Chama a função e recebe um parâmetro
        exibir_matriz(matriz_usuario)
    elif escolha == 5:
        # Chama a função e recebe um parâmetro
        somaDiagonal = somar_diagonal(matriz_usuario)
        print(f"A soma dos elementos acima da diagonal é {somaDiagonal}")
    # Caso nenhuma das opções válidas seja acionada, o terminal mostrará "Opção inválida"
    elif escolha != '':
        print('Opção inválida')
        escolha = menu()
        continue
    # Pergunta ao usuário se ele desejará ou não continuar
    continuar = input('Deseja continuar? [S/N]: ').strip().lower()[0]
    if continuar == 'n':
        break
    elif continuar == 's':
        # Caso a resposta comece com a letra "n" o programa irá retornar o usuário para o menu
        escolha = menu()
    else:
        # Caso o usuário digite algo diferente de "s" ou "n", o terminal irá mostrar opção inválida
        print('Opção inválida')
        # A variavel escolha será vazia para o retorno da variavel continuar
        escolha = ''
        continue
print('Programa encerrado!')
