n = int(input('Digite um número e lhe direi se é ou não primo: '))
total = 0
for c in range(1,n+1):
    if n % c == 0:
        print(f'\033[34m', end='')
        total += 1
    else:
        print('\033[m', end='')
    
    print(f'{c} ', end='')
if total == 2:
    print('O número só pode ser dividido duas vezes, portanto é um número primo!!!')
else:
    print("O número foi dividido por mais números entretanto não é um número primo!")