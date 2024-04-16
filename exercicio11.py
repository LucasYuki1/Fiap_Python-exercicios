n = int(input('Digite um número: '))
if n>=0:
    n/=2
    print(f'A metade do número n fornecido é {n}')
elif n<0:
    n**=n
    print(f'O quadrado do número n negativo é {n}')