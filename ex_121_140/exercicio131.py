numeros = []
while True:
        numero = input("Digite um número: ")
        if numero == '0':
            break
        numeros.append(numero)

with open ('arquivo.txt', 'w', encoding="utf-8") as arquivo:
    for a in numeros:
        arquivo.write(a + '\n')