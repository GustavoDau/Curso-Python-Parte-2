#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0
n = int(input('Digite um numero'))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end= '')
if cont == 2:
    print('o numero {} foi divisivel {} vezes, portanto ele eh primo'.format(n, cont, end=' '))
else:
    print('o numero {} foi divisivel por {} vezes, portanto ele nao eh primo'.format(n, cont, end=' '))