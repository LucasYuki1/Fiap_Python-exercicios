idades = []
for a in range(1,11):
    idade = int(input(f'Digite a {a}ª idade: '))
    idades.append(idade)
idades.sort()
print(f'As idades maiores ou iguais a 18 são: ', end='')
for none in idades:
    if none >= 18:
        print(f'{none}', end=', ')