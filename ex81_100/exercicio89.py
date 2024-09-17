import random

def milhao():
    numeros = []
    for a in range(1,10001):
        numeros.append(random.randint(1,6))
    for i in numeros:
        n1 = numeros.count(1)
        n2 = numeros.count(2)
        n3 = numeros.count(3)
        n4 = numeros.count(4)
        n5 = numeros.count(5)
        n6 = numeros.count(6)
    print(f'O número 1 aparece {n1}')
    print(f'O número 2 aparece {n2}')
    print(f'O número 3 aparece {n3}')
    print(f'O número 4 aparece {n4}')
    print(f'O número 5 aparece {n5}')
    print(f'O número 6 aparece {n6}')
milhao()