def ok(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
n = int(input(f'Digite um número: '))
print(f'O valor retornado é {ok(n)}')