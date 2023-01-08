from time import sleep
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
for c in range(11, 0, -1):
    print(c)
    sleep(1)
print('Boom!')

#Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += +1
        soma += c
    print(c, end=' ')
print('\na soma de todos os {} valores multiplos de 3 eh de {}'.format(cont, soma))

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Entre com 6 numeros diferentes'))
    if n % 2 == 0:
        soma += n
        cont += +1
print('voce informou {} numeros pares e a soma foi {}'.format(cont, soma))