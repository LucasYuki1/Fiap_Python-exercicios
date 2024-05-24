from random import randint
lista = []
lista_primo = []

for a in range(1,31):
    ver = 0
    numero = randint(1,50)
    lista.append(numero)
    for i in range(1,51):
        if numero % i == 0:
            ver += 1
    if ver == 2:
        lista_primo.append(numero)
print(sorted(lista_primo))
print(sorted(lista))
    