def palavras(palavra:str) ->int:
    ''' Quantidade de palavras existentes em uma frase '''
    algo = palavra.split()
    i = 0
    for a in algo:
        i += 1
    return print(f'Existem {i} palavras na sua frase')
palavras('sad as asd asd a')