def soma_divisores(a:int) -> int:
    '''Retorna a soma dos divisores do numero fornecido'''
    contador = 0
    for i in range(1, a+1):
        if a % i == 0:
            contador += i
            if a != i:
                print(i,end=" + ")
            else:
                print(i, "=", contador)
            
        
    return contador

print(soma_divisores(15))