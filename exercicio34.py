mul3 = int(input('Fonrneça um número e eu retornarei se é múltiplo de 3: '))
verificar = mul3%3
match verificar:
    case 0:
        print(f'O número é múltiplo de 3')
    case _:
        print('não é multiplo de 3')
        