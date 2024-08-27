# Parâmetro default (padrão)

def cadastrar_funcionario(nome:str='Não informado' , idade:int=0, salario:float=0.0) -> None:
    '''Retorna nome, idade e salário'''
    print('-' * 30)
    print(f"Nome: {nome}")
    print(f'Idade: {idade}')
    print(f'Salario: {salario}')

cadastrar_funcionario("Joao", ..., 3200)

# Parâmetro nomeado

cadastrar_funcionario(salario=2500)
