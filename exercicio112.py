def lista(numeros:list) -> list:
    ''' Retorna a quantidade de números pares e a soma dos ímpares '''
    par = impar = 0
    for i in numeros:
        if i % 2 == 0:
            par += 1
        else:
            impar += i
    return print(f'Quantidade de números pares: {par}\nSoma dos números ímpares: {impar}')

def pegarNumero() -> list:
    ''' Pega números e coloca em uma lista '''
    lis = []
    for a in range(1,11):
        ok = int(input(f'Digite um numero: '))
        lis.append(ok)
    lista(lis)  

pegarNumero()
