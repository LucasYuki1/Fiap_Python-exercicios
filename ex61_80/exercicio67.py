from random import randint
lista = []

while len(lista) <10:
    numero = randint(1,20)
    if numero not in lista:
        lista.append(numero)
    else:
        pass
print(sorted(lista))