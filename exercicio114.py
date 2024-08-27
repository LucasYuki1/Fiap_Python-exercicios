nomes = []
idades = []
while True:
    nome = input(f'Digite um nome "para sair deixe este campo vazio": ').strip()
    if nome == "":
        break
    idade = int(input(f'Digite uma idade utilize um número inteiro: '))
    nomes.append(nome)
    if idade >= 18:
        idades.append(idade)
print(f'As pessoas na lista são: ')
for a in nomes:
    print(a)

print(f'As pessoas maiores de idade tem respectivamente: \n{idades}')