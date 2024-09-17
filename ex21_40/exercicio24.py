a = float(input('Digite um valor: '))
b = float(input('Digite um valor: '))
c = float(input('Digite um valor: '))
if c>b>a:
    print(f'A ordem dos numeros digitado está crescente')
elif a>b>c:
    print(f'A ordem dos números está decrescente')
else:
    print(f'Está em uma ordem desordenada')