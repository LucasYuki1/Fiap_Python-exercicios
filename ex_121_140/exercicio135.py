ips = set()
with open('ips.txt', 'r', encoding="utf-8") as arquivo:
    for linha in arquivo:
        ips.add(linha)
    for a in ips:
        print(a)