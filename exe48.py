s=0
count = 0
for c in range(1,501,2):
    if c % 3 == 0:
        #contador
        count += 1
        #Acumulador
        s += c
        #end=' ' deixa na horizontal
        print(c, end=' ')
print('\nO valor total da somatória de {} números mútiplos de 3 entre 0 e 500 é {}'.format(count, s))
