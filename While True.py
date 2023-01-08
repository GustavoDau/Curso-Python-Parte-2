#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual
# foi a soma entre eles (desconsiderando o flag).

soma = cont = n = 0
while n != 999:
    cont += 1
    soma += n
    n = (int(input('Digite um numero ou 999 para finalizar o programa')))
    if n == 999:
        break
print(f'Voce digitou {cont} numeros e a soma deles foi {soma}')

soma = cont = n = 0
while True:
    n = (int(input('Digite um numero ou 999 para finalizar o programa')))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Voce digitou {cont} numeros e a soma deles foi {soma}')