nota = float(input('Digite a nota do aluno (os valores devem estar dentro do intervalo de 0 a 10): '))
nota2 = float(input('Digite a segunda nota do aluno (os valores devem estar dentro do intervalo de 0 a 10): '))
if nota >10 or nota<0:
    print(f'Você digitou uma nota inválida')
elif nota2 >10 or nota2<0:
    print(f'Você digitou uma nota inválida')
else:
    media = (nota+nota2)/2
    print(f'A média do aluno foi de {media}')