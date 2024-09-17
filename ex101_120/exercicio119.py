# Exercício 04
# Conte a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a    vogal e o valor é a quantidade de vezes que essa vogal aparece no texto.
# Exemplo:
# Para o texto abaixo:
# 'faculdade de tecnologia fiap'

def vogais(palavra:str) -> int:
    ''' Conta as vogais de uma frase '''
    algo = palavra.upper().split()
    a = e = i = o = u = 0
    
    for g in algo:
        a += g.count("A")
        e += g.count("E")
        i += g.count("I")
        o += g.count("O")
        u += g.count("U")

    dicionario = {'a' : a, 'e' : e , 'i': i, 'o':o,'u':u}
    return print(dicionario)

frase = input(f'Digite sua frase e será retornado a quantidade de vogais existentes nela: ')
vogais(frase)

