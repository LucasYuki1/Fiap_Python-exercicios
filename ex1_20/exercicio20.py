cont = 's'
while cont == 's':
    print('1-adição\n2-subtração\n3-divisão\n4-multiplicação')
    operacao = int(input('Selecione uma operação: '))
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    if operacao == 1:
        n3 = n1+n2
        print(f'A soma de {n1} com {n2} é {n3}')
    elif operacao == 2:
        n3 = n1-n2
        print(f'A subtração dos números {n1} com {n2} é {n3}')
    elif operacao == 3:
        if n1 == 0 or n2 == 0:
            print(f'Não é possível dividir por 0')
            exit()
        n3 = n1/n2
        print(f'O número {n1} por {n2} é equivalente a {n3}')
    elif operacao == 4:
        n3 = n1 * n2
        print(f'O produto de {n1} com {n2} é de {n3}')
    cont = str(input(f'Deseja continuar? [S/N] ')).strip().lower()[0]