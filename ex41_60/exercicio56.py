n = int(input('Digite um número: '))
limite = n
produto = 1
for a in range(1,n+1):
    print(f'{n}',end='')
    if a == limite:
        print(f' = ',end='')
    else:
        print(' x ',end='')
    produto*=n
    n-=1
print(produto)
    
    
