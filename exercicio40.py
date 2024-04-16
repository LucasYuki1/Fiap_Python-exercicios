n = int(input('Digite um número e retornarei se ele é perfeito ou não: '))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
    exit()  # Encerra o programa se o número não for positivo

soma_divisores = 0
divisores = []

# Encontrar todos os divisores próprios e calcular a soma
for i in range(1, n):
    if n % i == 0:
        soma_divisores += i
        divisores.append(i)

# Imprimir a lista de divisores próprios formatada com '+'
if divisores:
    print(' + '.join(map(str, divisores)), end=" ")

print(f"= {soma_divisores}")

# Verificar se o número é perfeito
if soma_divisores == n:
    print(f'O número {n} é um número perfeito.')
else:
    print(f'O número {n} não é um número perfeito.')
