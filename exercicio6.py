horas = int(input('Digite um valor para as horas: '))
minutos = int(input('Digite um valor para os minutos: '))
if 0<=horas<=24 and 0 <=minutos<=59:
    print(f'São {horas:02}:{minutos:02}')
else:
    print(f'São válidas horas entre 00:00 e 23:59')