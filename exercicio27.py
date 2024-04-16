preco = float(input("digite o preço do produto: "))
print(" 1-MG\n2-SP\n3-RJ\n4-MS")
estado = int(input("Selecione um estado: "))
if estado == 1:
    preco *= 1.07
    print(f"O preço final do produto para Minas Gerais será de {preco}")
elif estado == 2:
    preco *= 1.12
    print(f'O preço final do produto para São Paulo será de {preco}')
elif estado == 3:
    preco *= 1.15
    print(f'O preço final do produto destinado ao Rio de Janeiro será de {preco}')
elif estado == 4:
    preco *= 1.08
    print(f'O preço final do produto destinado para Mato Grosso do Sul será de {preco}')
else:
    print(f'Selecione um estado válido por favor')