def comprar_produto(produto:str='Não informado', quantidade:int=1) -> None:
    '''Retorna a mensagem do produto e quantidade adquirirdas'''
    print(f'Nome do produto: {produto}')
    print(f'Quantidade: {quantidade}')
comprar_produto("Detergente", 5)