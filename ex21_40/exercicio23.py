a = float(input('Digite o valor de um do primeiro lado do triângulo: '))
b = float(input('Digite o valor de um do segundo lado do triângulo: '))
c = float(input('Digite o valor de um do terceiro lado do triângulo: '))
if c > a+b:
    print(f'Com essas medidas não é possível formar um triângulo')
elif b > c+a:
    print(f'Com essas medidas não é possível formar um triângulo')
elif a > c+b:
    print(f'Com essas medidas não é possível formar um triângulo')
else:
    print(f'É possível formar um triângulo com essas medidas')