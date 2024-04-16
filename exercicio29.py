
n1 = int(input('digite um número inteiro: '))
n2 = int(input('digite um segundo número inteiro: '))
n3 = int(input('digite um terceiro número inteiro: '))
if n1<n2<n3:
    print(f'A ordem crescente é {n1, n2, n3}')
elif n3<n2<n1:
    print(f'A ordem crescente é {n3, n2, n1}')
else:
    if n3>n1:
        print(f'A ordem crescente é de {n1, n3, n2}')
    elif n1>n3:
        print(f'A ordem crescente é de {n3, n1, n2}')