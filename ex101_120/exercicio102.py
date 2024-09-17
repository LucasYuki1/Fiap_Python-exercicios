def concatenar_string(a:str='',b:str='', separador:str=' ') -> str:
    '''Concatena strings e coloca um separado'''
    stringConcatenada = a+separador+b
    return stringConcatenada
print(concatenar_string("algo", "Outro algo", "|"))