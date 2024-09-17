a = []
for b in range(0,3):
    nota = float(input(f'Digite a {b+1}ª nota: '))
    a.append(nota)

if sum(a)/3 < 6:
    print(f'O aluno foi reprovado com {sum(a)/3}')
else:
    print(f'O aluno foi aprovado com {sum(a)/3}')