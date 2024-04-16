x = float(input('Digite o valor de X: '))
if x <=1:
    x = 1
elif 1<x<=2:
    x = 2
elif 2<x<=3:
    x = x**2
else:
    x = x**3
print(f'{x:.1f}')