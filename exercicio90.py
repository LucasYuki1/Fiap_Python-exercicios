import math
def bhaskara(a,b,c):
    raiz = math.sqrt(b**2-4*a*c)
    x1 = (b + raiz)/2*a
    x2 = (b - raiz)/2*a
    print(f'A raíz 1 é: {x1}')
    print(f'A raíz 2 é: {x2}')
a = int(input(f'Defina o valor de "a": '))
b = int(input(f'Defina o valor de "b": '))
b = -b
c = int(input(f'Defina o valor de "c": '))
bhaskara(a,b,c)