from math import sqrt
n = int(input('Digite um número inteiro: '))
if sqrt(n)%2==0 or sqrt(n)%3==0 or sqrt(n)%5==0:
    print('O número {} não é um número primo'.format(n))
else:
    print('O número {} é primo'.format(n))