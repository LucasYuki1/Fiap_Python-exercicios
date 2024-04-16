qtd_aluno = int(input('Digite a quantidade de alunos que tem na sala: '))
qtd_nota = int(input('Digite a quantidade de notas: '))
media = 0
for a in range(1,qtd_aluno+1):
    media = 0
    for i in range(1,qtd_nota+1):
        n = int(input(f'Digite a {i}ª nota: '))
        media+=n
    media/=qtd_nota
    print(f'A média do {a}º foi de {media:.2f}')