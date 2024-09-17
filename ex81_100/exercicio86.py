import time
def main():
    print("""
    -=-=-=-=-=-=-=-=-=-=-=-=
    Calculadora:
    1-Adição
    2-Subtração
    3-Multiplicação
    4-Divisão
    5-Sair do programa
    =-=-=-=-=-=-=-=-=-=-=-=-=
    """)
    opcao = int(input(f'Selecione sua opção: '))
    if opcao == 1:
        adicao()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    else:
        print(f'Saindo do programa...')
        time.sleep(4)
        exit()
def adicao():
    n1 = int(input(f'Digite o primeiro valor: '))
    n2 = int(input(f'Digite o segundo valor: '))
    resultado = n1 + n2
    print(f'O resultado da operação é: {resultado}')
    main()
    
    
def subtracao():
    n1 = int(input(f'Digite o primeiro valor: '))
    n2 = int(input(f'Digite o segundo valor: '))
    resultado = n1 - n2
    print(f'O resultado da operação é: {resultado}')
    main()
    
    
def multiplicacao():
    n1 = int(input(f'Digite o primeiro valor: '))
    n2 = int(input(f'Digite o segundo valor: '))
    resultado = n1 * n2
    print(f'O resultado da operação é: {resultado}')
    main()
    
    
def divisao():
    n1 = int(input(f'Digite o primeiro valor: '))
    n2 = int(input(f'Digite o segundo valor: '))
    if n1 == 0 or n2 == 0:
        print(f'Não é possóvel dividir por zero tente novamente')
        main()
    if n1 < n2:
        resultado = n2/n1
        print(f'O resultado da operação é: {resultado}')
        main()
    else:
        resultado = n1/n2
        print(f'O resultado da operação é: {resultado}')
        main()
main()