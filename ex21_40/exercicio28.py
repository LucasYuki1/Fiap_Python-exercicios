km = float(input("Digite a distância em Km: "))
litros = float(input('Digite a quantidade de litros que foi gasta: '))
if litros/km < 8:
    print(f'Venda o carro')
elif 8<=litros/km <=14:
    print(f'Econômico')
else:
    print(f'Supereconômico')