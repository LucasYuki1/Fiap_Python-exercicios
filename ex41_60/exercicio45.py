import os
import time
saldo = []
def main():
    os.system('cls')
    opcoes()
def opcoes():
    print('1-Consultar saldo')
    print('2-Realizar saque')
    print('3-Realizar Depósito')
    print('4-Sair')
    try:   
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            consultarsaldo()
        elif opcao == 2:
            realizarSaque()
        elif opcao == 3:
            realizarDepósito()
        elif opcao == 4:
            sair()
        else:
            sair()
    except:
        erro()
def consultarsaldo():
    print(f'Você tem atualmente: R${sum(saldo)} na sua conta')
    time.sleep(3)
    main()
def realizarDepósito():
    try:
        os.system('cls')

        n = float(input('Quanto deseja depositar? '))
        if n < 0:
            print('não foi possível depositar um valor negativo')
            time.sleep(3)
            main()
        saldo.append(n)
        main()
    except:
        erro()
def realizarSaque():
    try:
        if sum(saldo) < 0:
            print(f'Não foi possível sacar por não haver saldo em sua conta')
        
        else:
            s = int(input('Quanto deseja sacar? '))
            if s < 0:
                print('Não foi possível fazer esse saque')
                time.sleep(3)
                main()
            novo_saldo = sum(saldo)-s
            print(f'O seu novo saldo após o saque é: R${novo_saldo}')
            time.sleep(3)
            main()
    except:
        erro()
def sair():
    os.system('cls')
    print(f'Saindo do Sistema...')
    exit()
def erro():
    print(f'Algo está errado, retornando para o menu inicial')
    time.sleep(3)
    main()
if __name__ == '__main__':
    main()