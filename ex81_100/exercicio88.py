def triangular(n):
    if n < 1:
        return False
    
    i = 1
    while i * (i + 1) * (i + 2) <= n:
        if i * (i + 1) * (i + 2) == n:
            return True
        i += 1
    
    return False
n1 = int(input('Digite um número, retornarei se é ou não triangular: '))
print(triangular(n1))