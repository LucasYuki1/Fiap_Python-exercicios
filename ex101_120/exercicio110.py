def tirarEspaco(palavra:str) -> str:
    ''' Tira os espaços da frase '''
    algo = palavra.split()
    for i in algo:
        print(i,end='')
tirarEspaco(" asd a sd asd as d ad as d asd as d asd asd as da sd as das d asds das d asd asd as das d asd as d")