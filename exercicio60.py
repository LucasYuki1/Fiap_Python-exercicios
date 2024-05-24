n = 1
n1 = int(input(f'Digite o primeiro parâmetro: '))
n2 = int(input(f'Digite o segundo parâmetro: '))
for a in range(n1,n2+1):
    tot = 0
    for a in range(n1,n2+1):
        if n % a == 0:
            tot+=1
            print('\033[34m', end='')
        else:
            print('\033[m', end='')
        
    if tot == 2:
        print(f'{a}', end='-')
    if a == n + 1:
        print('Acabou')
    n+=1