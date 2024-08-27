def numero(numeros:list) -> list:
    ''' Retorna o maior numero da lista, o menor e a média dos 10 numeros '''
    return print(f'''
O maior número é: {max(numeros)}
O menor número é: {min(numeros)}
A média dos números é: {sum(numeros)/10}
''')
lista = []
for a in range(1,11):
    b = int(input(f'Digite um número: '))
    lista.append(b) 
numero(lista)