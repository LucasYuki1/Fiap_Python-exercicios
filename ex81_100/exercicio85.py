

def ler_numero():
    n = int(input(f'Digite um número e retornarei sua tabuada: '))
    tabuada(n)
def tabuada(n):
    for a in range(1,11):
        print(f'{n} * {a} = {n*a}')
ler_numero()
