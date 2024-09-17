estado_civil = str(input('Digite o seu estado civil\nS-Solteiro\nC-Casado\nV-Viúvo\nD-Divorciado: ')).strip().lower()[0]
match estado_civil:
    case "s":
        print(f'Você é solteiro')
    case "c":
        print(f'Você é casado')
    case "v":
        print(f'Você é viúvo')
    case "d":
        print(f'Você é divorciado')
    case _:
        print(f'Opção inválida')