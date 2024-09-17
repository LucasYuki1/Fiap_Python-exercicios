n = int(input('Digite um número, retornarei se é primo ou não: '))
tot = 0
for a in range(1,n+1):
    if n % a == 0:
        tot+=1
        print('\033[33m', end='')
    else:
        print('\033[32m', end='')
    print(f'{a} ', end='')
if tot == 2:
    print(f'\nO número é primo')
else:
    print(f'\nO número não é primo') 