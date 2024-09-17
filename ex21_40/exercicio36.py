codigo = int(input('Digite o código da comida:\n1-Picanha R$25,00\n2-Lasanha R$20,00\n3-Strogonoff R$20,00\n4-Bife AceboladoR$15,00\n5-Pão com Ovo R$5,00: '))
gorjeta = str(input(f'Você aceita dar gorjeta para o garçom (10%)? [S/N] ')).strip().lower()[0]
match codigo:
    case 1:
        match gorjeta:
            case 's':
                print(f'Sua conta total ficou R${25*1.10}')
            case 'n':
                print(f'Sua conta total foi de R${25},00')
    case 2:
        match gorjeta:
            case 's':
                print(f'Muito obrigado a sua conta total foi de R${20*1.1}')
            case 'n':
                print(f'Sua conta total foi de R${20},00')
    case 3:
        match gorjeta:
            case 's':
                print(f'Muito obrigado a sua conta total foi de R${20*1.1}')
            case 'n':
                print(f'Sua conta total foi de R${20},00')
    case 4:
        match gorjeta:
            case 's':
                print(f'Muito obrigado a sua conta total foi de R${15*1.1}')
            case 'n':
                print(f'Sua conta total foi de R${15},00')
    case 5:
        match gorjeta:
            case 's':
                print(f'Muito obrigado a sua conta total foi de R${5*1.1}')
            case 'n':
                print(f'Sua conta total foi de R${5},00')
    case _:
        print(f'Selecione uma opção válida')