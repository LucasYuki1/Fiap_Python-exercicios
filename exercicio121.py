# Exercício 2
# Crie uma lista de tuplas, onde cada tupla contém informações sobre um aluno: (Nome do aluno, Idade, Nota)
# Escreva uma função chamada 'alunos_aprovados' que recebe a lista de alunos e retorna uma nova lista apenas com os nomes dos alunos que têm uma nota maior ou igual a 7.
# Exemplo da estrutura a ser criada:
# alunos = [('Alice', 20, 8.5), ('Bob', 18, 5.0), ('Eva', 22, 7.5)]
# Exemplo de Retorno:

# alunos = {[("Alice", 20, 8.5), ("Bob", 18, 5.0), ('Eva', 22, 7.5)], [("Alice", 20, 8.5), ("Bob", 18, 5.0), ('Eva', 22, 7.5)]}
aprovados = []

alunos = {"554499": {
    'Python' : (9.5, 8),
    'Java' : (10, 9)
}}

# print(sum(alunos['554499']['Nota1'])/2)

for value in alunos.values():
    for key, value1 in value.items():
        print(f'{key}: {value1}')
        print(f'Média: {sum(value1)/2}')

def alunos_aprovados(alunos:list) -> list:
    ''' Após fornecer a lista com os alunos pega as variáveis e fornece os alunos que passaram '''
    for nome, idade, nota in alunos:
        if nota >= 7.0:
            aprovados.append(nome)
    print("Os alunos aprovados:")

    for a in aprovados:
        print(f'Aluno(a) aprovado(a): {a}')
alunos_aprovados(alunos)