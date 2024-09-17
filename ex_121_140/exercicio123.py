# Crie um dicionário chamado pessoas que contenha informações sobre pessoas. - Chave: cpf da pessoa
# - Valor: dicionário contendo nome, idade e cidade.
# Adicione pelo menos 5 pessoas ao dicionário.
# Crie uma função chamada 'pessoas_cidade' que exibe o nome de todas as pessoas que moram em uma cidade específica.
# Exemplo da estrutura a ser criada: 
pessoas = {
 '123.888.999-89': {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}, 
 '845.678.658-02': {'nome': 'Bob', 'idade': 30, 'cidade': 'Rio de Janeiro'}, 
 '555.781.657-12': {'nome': 'Eva', 'idade': 22, 'cidade': 'São Paulo'},
 '666.777.788-21': {'nome': 'Joao', 'idade': 32, 'cidade': 'Amazonas'},
 '777.888.999.31': {'nome': 'Evandro', 'idade': 41, 'cidade': 'Amapá'}
 } 

def pessoas_cidade(pessoas:dict, cidade:str) -> None:
    for pessoa in pessoas.values():
        if pessoa['cidade'].lower() == cidade.lower():
            print(f"-Morador de {cidade}: {pessoa['nome']}")
            
busca = input('Digite a cidade que queira fazer a busca: ')
pessoas_cidade(pessoas, busca)