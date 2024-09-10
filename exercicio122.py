# Exercício 3
# Crie um dicionário chamado 'estoque' com informações sobre alguns produtos: - Chave: Nome do produto
# - Valor: Tupla contendo preço e quantidade em estoque
# Adicione pelo menos 5 produtos ao dicionário.
# Crie uma função chamada 'total_valor_estoque' que calcula o valor total do estoque (preço * quantidade) para todos os produtos no dicionário.
# Exemplo da estrutura a ser criada:
# estoque = {'caneta': (4.70, 40), 'caderno': (45.0, 20), 'lápis': (3.50, 10)}



def total_valor_estoque() -> float:
    ''' Pega um dicionário e retorna um float com os valores totais '''
    estoque = {}
    vezes = int(input('Quantos produtos deseja adicionar? '))
    for _ in range(vezes):
        nome_prod = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: '))
        quantidade = int(input('Digite a quantidade do estoque: '))
        estoque[nome_prod] = (preco, quantidade)

    valor_total = 0.0
    for preco, quantidade in estoque.values():
        valor_total += (preco * quantidade)
        print(f'O valor total do {nome_prod} no estoque é de: {valor_total}')
total_valor_estoque()