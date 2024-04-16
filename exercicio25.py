idade = int(input(f'Digite a sua idade: '))
contribuicao = int(input(f'Digite por quantos anos você contribuiu: '))
if idade >= 60 and idade<65:
    if contribuicao >= 25 and contribuicao <30:
        print(f'Você está nos requisitos para se aposentar')
    else:
        print(f'Você não pode se aposentar ainda')
elif idade >= 65:
    print(f'Você pode se aposentar')
elif contribuicao>=30:
    print(f'Parabéns por seu trabalho ao longo dos anos, você já pode se aposentar sem preucupações')
else:
    print(f'Você não pode se aposentar ainda')