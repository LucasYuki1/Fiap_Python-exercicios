parametro = int(input(f'Digite qual número você deseja que seja contado: '))
lista = []
for m in range(1,11):
    num = int(input(f'Digite um número: '))
    lista.append(num)
procurar = l7(parametro)
print(f'Foram digitados {procurar} números dentro do seu parâmetro')