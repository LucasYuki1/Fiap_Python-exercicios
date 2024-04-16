n = int(input('Digite a quantidade de números ímpares que você quer que seja exibido na tela: '))
cont = 0
impar =1 
while cont < n:
    
    print(f'{impar}', end='-')
    cont+=1
    impar+=2
if cont == n:
    print('acabou')