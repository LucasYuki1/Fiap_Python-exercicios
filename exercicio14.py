n = int(input('Digite um valor inteiro entre 1 e 999: '))
if n < 1 or n >999:
    print(f'Número inválido, por favor tente outro')
else:
    u = n%10
    d = ((n%100) - (n%10))//10
    c = n - (n%10)
    c = n - ((n%100))
    c//=100
    print(f'A soma dos algarismos do número fornecido é de {u+d+c} ({c}+{d}+{u})')