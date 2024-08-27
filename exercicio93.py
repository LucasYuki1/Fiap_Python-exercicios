def quadrado (x:int)->int:
    '''Retorna o quadrado do valor fornecido'''
    y = x**2
    return y
print(quadrado(7))

# Próximo ex

def somaQuadrado(y:int, z:int) -> int:
    '''Retorna a soma dos quadrados'''
    w = quadrado(y) + quadrado(z)
    return w