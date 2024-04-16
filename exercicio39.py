x = int(input('Digite um número do primeiro valor: '))
y = int(input('Digite o ultimo número para o retorno do intervalo: '))
if x < y:
    cont = x
    while cont<=y:
        if cont % 2 != 0:
            print(f'{cont}', end=', ')
        cont+=1
elif y < x:
    cont = y
    while cont<=x:
        if cont % 2 != 0:
            print(f'{cont}', end=', ')
        cont+=1
else:
    print('ERRO')
if cont == x:
    print('Acabou')
else:
    print('acabou')