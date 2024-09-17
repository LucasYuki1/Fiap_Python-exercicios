numeros_pares = []
numeros_impares = []
while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            break
        if numero % 2 == 0:
            numeros_pares.append(str(numero))
        else:
            numeros_impares.append(str(numero))
try:
    with open ('arquivo_par.txt', 'w', encoding="utf-8") as arquivo:
        for a in numeros_pares:
            arquivo.write(a + '\n')
    with open ('arquivo_impar.txt', 'w', encoding="utf-8") as arquivo:
        for a in numeros_impares:
            arquivo.write(a + '\n')
except FileNotFoundError:
    print("Arquivo não encontrado")