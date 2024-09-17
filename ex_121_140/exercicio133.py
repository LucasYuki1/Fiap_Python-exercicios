numeros_impares = []
numeros_pares = []

# Lendo os números ímpares e convertendo para inteiros
with open('arquivo_impar.txt', 'r', encoding="utf-8") as arquivo:
    for linha in arquivo:
        a = linha.strip()  # Remove o '\n'
        numeros_impares.append(int(a))  # Converte para inteiro

# Lendo os números pares e convertendo para inteiros
with open('arquivo_par.txt', 'r', encoding="utf-8") as arquivo:
    for linha in arquivo:
        a = linha.strip()  # Remove o '\n'
        numeros_pares.append(int(a))  # Converte para inteiro

# Juntando as duas listas
numeros_impares.extend(numeros_pares)

# Ordenando os números (agora como inteiros)
numeros_impares.sort()

# Escrevendo a lista ordenada no arquivo
with open('arquivo_sort.txt', 'w', encoding="utf-8") as arquivo:
    for a in numeros_impares:
        arquivo.write(str(a) + '\n')  # Converte de volta para string ao escrever
