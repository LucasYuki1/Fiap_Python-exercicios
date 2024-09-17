salario = float(input(f'Digite o valor so salário da pessoa: '))
prestacao = float(input(f'Digite o valor da prestação: '))
if prestacao > salario*0.2:
    print(f'Empréstimo não concedido')
else:
    print(f'Empréstimo concedido')