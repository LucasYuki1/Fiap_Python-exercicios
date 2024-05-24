
pi = 3.14
def area(n):
    área = pi * (n*n)
    return área
def perimetro(n1):
    perímetro = pi * 2 * n1
    return perímetro

raio = float(input(f'Digite o raio do círculo: '))
a = area(raio)
p = perimetro(raio)
print(f'A área desse círculo é de {a} e o perímetro é de {p}')