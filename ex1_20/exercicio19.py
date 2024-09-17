bmaior = float(input('Digite a base maior do trapézio: '))
bmenor = float(input('Digite a base menor do trapézio: '))
altura = float(input('Digite a altura do trapézio: '))
if bmaior <=0 or bmenor<= 0 or altura <= 0:
    print(f'Não existe uma lado com 0 ou menos')
    exit()
else:
    a = ((bmaior+ bmenor)*altura)/2
    print(f'A área do trapézio é de {a}')