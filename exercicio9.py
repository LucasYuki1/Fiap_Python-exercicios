l1 = int(input('Digite um lado do triângulo: '))
l2 = int(input('Digite um outro lado do triângulo: '))
l3 = int(input('Digite o último lado do triângulo: '))
if l1 ==l2 ==l3:
    print(f'Este é um triângulo equilátero')
elif l1==l2 and l1 or l2 != l3:
    print(f'Este é um triângulo isósceles')
else:
    print(f'Este é um triângulo escaleno')