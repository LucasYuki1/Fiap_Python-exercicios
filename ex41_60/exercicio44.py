impar = []
par = []
n = 1
produtoim = 1
while n!=0:
    try:
        n = int(input('Digite um número: '))
        if n % 2 == 0:
            par.append(n)
        else:
            impar.append(n)
    except:
        print('Insira um valor correto')
print(f'A soma de todos os números pares é de: {sum(par)}')
for c in impar:  
    produtoim *= c
print(f'o resultado da multiplicação dos números ímpares é de: {produtoim}')

    
