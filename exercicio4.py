str = str(input('Digite uma letra: ')).strip().upper()[0]
if str in "AIUEO":
    print(f'A letra digitada é vogal')
else:
    print('A letra é uma consoante')