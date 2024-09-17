from random import randint
lista = []

for a in range(1,31):
    numero = randint(1,50)
    lista.append(numero)
multiplicador = int(input("digite um número para multiplicar: "))
print(lista)
for i in lista:
    valor = i * multiplicador
    
    print(valor, end= '-')
    