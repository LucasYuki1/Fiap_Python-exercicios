def verificar(n1, n2, n3):
    if n1 + n2 == n3:
        return True
    elif n1 + n3 == n2:
        return True
    elif n2 + n3 == n1:
        return True
    else:
        return False

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
print(verificar(n1,n2,n3))