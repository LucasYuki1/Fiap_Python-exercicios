code = int(input('Digite o código do produto 100~104'))
qtd = int(input('Quantas unidades irá querer? '))
if code == 100:
    cq = 13.20
    total = cq * qtd
    print(f'Ccachorro quente {qtd} unidades: {total}')
elif code == 101:
    hg = 19.90
    total = hg * qtd
    print(f'Hamburguer {qtd} unidades: {total}')
elif code == 102:
    cb = 21.90
    total = cb*qtd
    print(f'Chesseburguer {qtd} unidades: {total}')
elif code == 103:
    sn = 7
    total = sn*qtd
    print(f'Suco natural {qtd} unidades: {total}')
elif code == 104:
    r = 6.50
    total = r*qtd
    print(f'refrigerante {qtd} unidades: {total}')

