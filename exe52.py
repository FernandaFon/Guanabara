amarelo = '\033[33m'
vermelho = '\033[31m'
reset = '\033[0m'
count = 0

n = int(input('Digite um número inteiro: '))
for c in range(1,n+1):
    if n%c==0:
        print(f"{amarelo}{c}{reset}", end=' ')
        count += 1
    else:
        print(f"{vermelho}{c}{reset}", end=' ')

print('\nO número {} foi dividido {} vezes'.format(n,count), end=' ')

if count == 2:
    print('e por isso ele é primo')
else:
    print('e por isso ele não é primo')

print(f"\n{reset}Os números em {vermelho}vermelho{reset} não são divisiveis.")
print(f"{reset}Os números em {amarelo}amarelo{reset} são divisiveis")