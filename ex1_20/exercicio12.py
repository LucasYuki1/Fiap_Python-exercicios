n = int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))
if n > n1:
    d = n-n1
    print(f'O maior valor entre os números digitados é {n} e a diferença dos dois é {d}')
elif n1 > n:
    d = n1-n
    print(f'O maior valor entre os números digitados é {n1} e a diferença dos dois é {d}')