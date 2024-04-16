media = []
for n in range(1,4):
    nota = float(input(f'Digite a {n}ª nota (números válidos 0->10): '))
    if nota < 0 or nota >10:
        print(f'Digite uma nota válida')
        exit()
    if n == 1:
        nota*=2
    elif n == 2:
        nota*=3
    elif n ==3:
        nota*=5
    media.append(nota)
if sum(media)/10<4:
    print(f'O aluno foi reprovado com {sum(media)/10:.1f} de média')
elif sum(media)/10>=4 and sum(media)/10 <6:
    print(f'O aluno está de recuperação com {sum(media)/10:.1f} de média')
elif sum(media)/10>=6:
    print(f'O aluno foi aprovado com {sum(media)/10:.1f} de média')
else:
    print('erro')