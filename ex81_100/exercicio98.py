def mostrar_informacoes(nome:str='Não informado', idade:int=0, cidade:str='não informado') -> None:
    '''Retorna as informações do cidadão'''
    print(f'Nome: {nome}')
    print(f'Idade: {idade}')
    print(f'Cidade: {cidade}')
mostrar_informacoes("João", 32, "São Paulo")