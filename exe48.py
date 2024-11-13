s=0
for c in range(0,501,3):
    if c % 2 == 1:
        s = s+c
        print(c)
print('O valor total da somatória de todos os mútiplos de 3 entre 0 e 500 é {}'.format(s))
