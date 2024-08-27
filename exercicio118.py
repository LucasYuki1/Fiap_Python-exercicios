alunos = {}
for a in range(5):
    rm = input(f'Digite seu RM: ')
    if rm == '':
        print('RM vazio detectado, encerrando o programa...')
        break  # Encerra o loop se RM estiver vazio

    notas = []
    for i in range(3):
        try:
            nota = float(input(f'Digite a {i+1}ª nota: '))
            notas.append(nota)
        except ValueError:
            print(f'Valor inválido fornecido, interrompendo o fluxo...')
            break  # Encerra o fluxo de notas em caso de erro

    if len(notas) == 3:  # Garante que três notas foram inseridas antes de calcular a média
        media = sum(notas) / 3
        alunos[rm] = media

# Exibe a média dos alunos
for rm, media in alunos.items():
    print(f'A média do aluno com RM {rm} é {media:.2f}')
