n = int(input('Digite quantas idades deseja colocar: '))
cont = 1
somaidade = 0
while cont<= n:
    idade = int(input(f'Digite a {cont}ª idade: '))
    cont+=1
    if cont != n:
        somaidade+=idade
    
print(f'A média das idades das pessoas é {(somaidade)/n}')