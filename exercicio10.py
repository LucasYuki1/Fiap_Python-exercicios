salário = int(input('Digite o salário fixo do trabalhador: '))
vendas = int(input('Digite quanto tevede ganho em vendas: '))
if vendas <= 1500:
    vendas*=0.03
    salário+=vendas
elif vendas > 1500:
    salário += (vendas*0.03)
    salário
