n = int(input('Digite um número: '))
for a in range(1,n+1):
    if n % a == 0:
        print(f'O divisor de {n} é: {a}')
    