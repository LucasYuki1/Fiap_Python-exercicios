with open('arquivo.txt', 'r') as arquivo:
    # Lê cada linha, remove o '\n', converte para inteiro e soma os números
    soma = sum(int(linha.strip()) for linha in arquivo)
print(f'A soma dos números no arquivo é de: {soma}')