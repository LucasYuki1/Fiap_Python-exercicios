def media(nota1,nota2):
    média = (nota1 + nota2)/2
    if média >= 6:
        print(f'O aluno foi aprovado com {média}')
    else:
        print(f'O aluno foi reprovado com {média}')
n1 = int(input(f'Digite a primeira nota: '))
n2 = int(input(f'Digite a segunda nota: '))
media(n1,n2)