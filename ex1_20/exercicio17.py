media = []
for n in range(1,4):
    nota = float(input(f'Digite a {n}ª nota: '))
    
    if n == 3:
        nota*=2
    media.append(nota)

print(f'A média ponderada do aluno foi de {sum(media)/4:.1f}')
if sum(media)/4 > 6:
    print(f'O aluno foi aprovado')
else:
    print(f'O aluno foi reprovado')