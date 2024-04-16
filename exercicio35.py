codigo = int(input(f'Digite o código necessário:\n1-Linux\n2-Banco de dados\n3-Windows Server\n4-Lógica e programação: '))
match codigo:
    case 1:
        print(f'A palestra está localizada no auditório 1')
    case 2:
        print(f'A palestra está localizada no auditório 2')
    case 3:
        print(f'A palestra está localizada no auditório 3')
    case 4:
        print(f'A palestra está localizada no auditório principal')
    case _:
        print(f'Opção inválida, por favor tente outra')