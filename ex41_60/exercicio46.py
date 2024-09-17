print('1 - Candidato 1')
print('2 - Candidato 2')
print('3 - Candidato 3')
print('4 - Voto em Branco')
print('5 - Finalizar')
tot = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0
branco = 0
while True:
    voto = int(input('Informe seu voto: '))
    if voto == 1:
        candidato1 += 1
        tot+=1
    elif voto == 2:
        candidato2 += 1
        tot+=1
    elif voto == 3:
        candidato3 += 1
        tot+=1
    elif voto == 4:
        branco += 1
        tot+=1
    elif voto == 5:
        break
    else:
        print('Por favor digite um valor válido')
print(f'O total de votos no candidato 1 foi: {candidato1}')
print(f'O total de votos no candidato 2 foi: {candidato2}')
print(f'O total de votos no candidato 3 foi: {candidato3}')
porcento = (branco/tot) * 100
if porcento > 0:
    print(f'A porcentagem de votos em branco foi de {porcento:.2f}%')
else:
    print('Não houve votos em branco')

# Determinar o vencedor com base nos votos recebidos por cada candidato
if candidato1 > candidato2 and candidato1 > candidato3:
    print('O candidato 1 foi o vencedor')
elif candidato2 > candidato1 and candidato2 > candidato3:
    print('O candidato 2 foi o vencedor')
elif candidato3 > candidato1 and candidato3 > candidato2:
    print('O candidato 3 foi o vencedor')
else:
    print('Houve um empate ou nenhum candidato recebeu votos suficientes para ser o vencedor')
