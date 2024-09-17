numeros = []

for a in range(10):
        numero = input("Digite um número: ")
        numeros.append(numero)

with open ('arquivo.txt', 'w', encoding="utf-8") as arquivo:
    for a in numeros:
        arquivo.write(a + '\n')