def calcular_salario(salario: float)->float:
    """Recebe um salário comom parâmetro e faz o cálculo do aumento"""
    if salario > 2000:
        salario *= 1.07
    elif salario < 2000 and salario > 0:
        salario *= 1.15
    else:
        print("Valor inválido fornecido")
    return salario
print(f'{calcular_salario(101):.2f}')