s = 0
for c in range(6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print('O somatorio de todos os números pares é igual a {}'.format(s))
