n = int(input("Digite um número inteiro e positivo: "))
soma = 0
while n > 0:
    digito = n % 10
    soma+=digito
    n //= 10
print(f'A soma total dos algarismos é de {soma}')