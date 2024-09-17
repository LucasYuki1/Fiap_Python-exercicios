par = []
impar = []
for a in range(0,10):
    num = int(input(f'Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'A lista de numeros pares é {par} e dos ímpares é {impar}')