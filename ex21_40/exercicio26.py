from math import ceil

largura = float(input("Digite a largura do cômodo: "))
comprimento = float(input("Digite o comprimento do cômodo: "))
altura = float(input("Digite a altura do cômodo: "))

# Área do teto
teto = largura * comprimento

desconsiderar = []

cont = input("Você deseja informar a área das janelas (s/n)? ").lower()
while cont == "s":
    altura_janela = float(input("Digite a altura da janela: "))
    comprimento_janela = float(input("Digite o comprimento da janela: "))
    desconsiderar.append(altura_janela * comprimento_janela)
    cont = input("Deseja informar mais alguma janela (s/n)? ").lower()

cont = input("Você deseja informar a área das portas (s/n)? ").lower()
while cont == "s":
    altura_porta = float(input("Digite a altura da porta: "))
    comprimento_porta = float(input("Digite o comprimento da porta: "))
    desconsiderar.append(altura_porta * comprimento_porta)
    cont = input("Deseja informar mais alguma porta (s/n)? ").lower()

# Área das paredes
parede12 = largura * altura
parede34 = comprimento * altura

# Área total a ser pintada
area_total = teto + 2 * (parede12 + parede34)

# Considerando a cobertura da tinta de 1 litro para cada 3 metros quadrados
litros_tinta = area_total / 3 

# Desconsiderando áreas das janelas e portas
area_desconsiderada = sum(desconsiderar)
litros_final = ceil(litros_tinta - area_desconsiderada)

print(f'Serão necessários {litros_final} litros de tinta.')
