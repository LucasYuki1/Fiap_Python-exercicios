salario = 2000
aumento = 0.015

for a in range(2016, 2025):
    salario += (salario*aumento)
    aumento*=2
    print(f'O salário no ano de {a}: R${salario:.2f}')