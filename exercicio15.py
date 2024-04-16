n = int(input(f'Digite um número com 3 algarismos (qualquer valor entre 100 e 999): '))
if n <100 or n>999:
    print(f'Por favor Digite um valor válido')
    exit()
u = n%10
d = ((n%100) - (n%10))//10
c = n - (n%10)
c = n - ((n%100))
c//=100
if u == c:
    print(f'O número digitado é uma capicua')
else:
    print(f'O número não é uma capicua')