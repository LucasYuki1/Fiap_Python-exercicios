valor = int(input('Digite o que deseja fazer\n1-Dobro\n2-Metade\n3-10% do número: '))
num = float(input('Digite o valor que sofrerá as alterações: '))
match valor:
    case 1:
        num*=2
        print(f'O dobro do valor fornecido é {num}')
    case 2:
        num/=2
        print(f'A metade do número fornecido é {num:.2f}')
    case 3:
        num *= 0.1
        print(f'10% do valor é: {num:.2f}')
    case _:
        print(f'Opção inválida')