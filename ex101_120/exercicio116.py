info = {}
for a in range(5):
    cpf = int(input(f'Digite seu CPF: '))
    if cpf == '':
        break
    else:
        ...
    nome = input(f'Digite seu nome: ')
    info[cpf] = nome
for chave, nome in info.items():
    print(f'Pessoa com o CPF {chave}, se chama: \n {nome}')
