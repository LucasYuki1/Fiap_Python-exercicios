pali = str(input('Digite uma frase: ')).strip().upper()
palavras = pali
junto = ''.join(palavras)
inverso = ''
print(f'Você digitou a frase {pali}')
#inverso  = junto[::-1]
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra]
if inverso == junto:
        print('A frase digitada é um palíndromo')
else:
        print('A frase digitada não é um palíndromo')