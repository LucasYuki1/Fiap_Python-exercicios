def pessoa(altura,sexo):
    if sexo == 'M':
        peso = (72.7 * altura) - 58
        return peso
    elif sexo == "F":
        peso = (62.1 * altura) - 44.7
        return peso
altura = float(input(f'Digite a altura da pessoa: '))
sexo = input(f'Digite o sexo da pessoa: [F/M]').strip().upper()[0]
print(f'O peso ideal da pessoa informada é {pessoa(altura,sexo):.2f}')
