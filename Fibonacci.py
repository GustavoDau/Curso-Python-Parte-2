#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N
# primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Quantos termos voce quer mostrar'))
n1 = 0
n2 = 1
print('{} - {}'.format(n1, n2), end='')
cont = 3
while cont <= n:
    n3 = n1 + n2
    print(' - {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    cont += 1