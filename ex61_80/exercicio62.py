par = []
media = []
for a in range(0,10):
    num = int(input(f'Digite um número: '))
    par.append(num)
    media.append(num)
print(f'A média dos números é de {(sum(media))/10} e a soma dos pares é {sum(par)}')