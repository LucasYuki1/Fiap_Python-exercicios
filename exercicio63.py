import random
numeros = []
for a in range(1,21):
    x = random.randint(1,50)
    numeros.append(x)
print(f'Os números contidos na lista são: {numeros}')
print(f'O somatório é: {sum(numeros)}')
print(f'O maior valor é: {max(numeros)}')
print(f'O menor número da lista é: {min(numeros)}')
