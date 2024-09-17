def caracteres(palavra:str) -> int:
    ''' Obtém uma palavra como parâmetro e retorna o número de caracteres '''
    algo = palavra.split()
    i = 0
    for letra in algo:
        for j in letra:
            i += 1
    return print(f'A quantidade de letras que tem é: {i}')

caracteres("lucas")