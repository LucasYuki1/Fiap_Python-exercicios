produtos = {}
for a in range(5):
    produto = input('Digite o nome do produto: ')
    if produto == '' or if produto in produtos:
        print(f'Você não digitou um nome ou tentou cadastrar um item já cadastrado! cancelando o cadastro')
    else:
        ...
    preco = float(input(f'Digite o preço do produto: '))
    produtos[produto] = preco

for chave, preco in produtos.items():
    if preco > 50:
        print(f'O produto {chave}, custa {preco}')
    