n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
if n1 <n2 <n3:
    print(f'O número {n1} é o menor')
elif n2<n1<n3:
    print(f'O número {n2} é o menor')
elif n3<n2<n1:
    print(f'O número {n3} é o menor')
else:
    print(f'Os números são iguais')