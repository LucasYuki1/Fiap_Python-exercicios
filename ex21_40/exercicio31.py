cliente = int(input('Digite se é:\ncliente comum[1]\ncliente vip[2]\nfuncionário[3]\n: '))
compra = float(input('Digite o valor total da compra: '))
match cliente:
    case 1:
        print(f'Cliente comum irá pagar o valor integral que é {compra}')
    case 2:
        print(f'Cliente VIP pagará com 5% de desconto\nTotal = {compra*0.95:.2f}')
    case 3:
        print(f'Funcionário paga 15% a menos\nTotal a ser pago será de: {compra*0.85:.2f}')
    case _:
        print(f'Opção inválida')