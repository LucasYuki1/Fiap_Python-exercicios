n = 1
for a in range(1,1000001):
    tot = 0
    for a in range(1,n+1):
        if n % a == 0:
            tot+=1
            print('\033[34m', end='')
        else:
            print('\033[m', end='')
        
    if tot == 2:
        print(f'{a}', end='-')
    n+=1