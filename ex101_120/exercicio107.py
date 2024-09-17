def vogais(palavra:str) -> int:
    ''' Conta as vogais de uma frase '''
    algo = palavra.upper().split()
    print(algo)
    a = e = i = o = u = 0
    for g in algo:
        a += g.count("A")
        e += g.count("E")
        i += g.count("I")
        o += g.count("O")
        u += g.count("U")
    return print(f'''
A quantidade de letras "a" é de: {a}
A quantidade de letras "e" é de: {e}
A quantidade de letras "i" é de: {i}
A quantidade de letras "o" é de: {o}
A quantidade de letras "u" é de: {u}
''')
vogais("a ae i o o o u u i ")