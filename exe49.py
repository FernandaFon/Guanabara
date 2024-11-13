n = int(input('Digite um número inteiro: '))
print('Tabuada de {}'.format(n))
for c in range(0,11):
    print('{} x {} = {}'.format(n,c,c*n))
print('FIM')
