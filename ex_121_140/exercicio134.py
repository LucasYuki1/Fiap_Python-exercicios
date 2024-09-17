alunos = int(input("Quantos alunos você deseja adicionar a nota? "))

# Abrir o arquivo para escrita e adicionar as notas
with open('notas_alunos.txt', 'w', encoding="utf-8") as arquivo:
    for i in range(alunos):
        nome = input("Digite o nome do aluno: ")
        arquivo.write(f'{nome}: ')
        for j in range(4):
            nota = float(input(f"Digite a {j+1}ª nota: "))
            arquivo.write(f'{nota} ')
        arquivo.write('\n')

# Abrir o arquivo para leitura e calcular as médias
with open('notas_alunos.txt', 'r', encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista = linha.split()  # Divide a linha em uma lista
        aluno = lista[0]  # Nome do aluno é o primeiro item
        notas = [float(nota) for nota in lista[1:]]  # Converter as notas restantes para float
        
        # Calcular a média das notas
        media = sum(notas) / len(notas)
        
        # Exibir a média do aluno
        print(f'A média do aluno {aluno} foi de {media:.2f}')
