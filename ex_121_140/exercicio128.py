python = {"joao", 'ana', 'lucas', 'nicolas', 'eduardo', 'alice'}
java = {'lucas', 'leonardo', 'paulo'}
for i in python:
    print(f"Aluno de python: {i}")
for i in java:
    print(f"Aluno de Java: {i}")
print(f'Alunos que frequentam ambos cursos: {python.intersection(java)}')
print(f'Alunos que frequentam pelo menos um dos cursos: {python.union(java)}')