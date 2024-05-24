def poligono(numero):
    match numero:
        case 3:
            print(f'O polígono é um triângulo')
        case 4:
            print(f'O polígono é um quadrado')
        case 5:
            print(f'O polígono é um pentágono')
        case _:
            print(f'Nenhuma opção válida foi selecionada')
numero = int(input(f'Digite quantos lado tem o polígono: '))
poligono(numero)