# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.

resposta = 's'
cont = 0
soma = 0
n = 0
maior = 0
menor = 0
while resposta in 'Ss':
    n = int(input('Digite um numero'))
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('voce deseja continuar? s/n')).upper().strip()[0]
print('''foram digitados {} numeros, a soma deles foi {}, e a media foi de {: .2f}
o maior numero digitado foi {} e o menor numero digitado foi {}'''.format(cont, soma, media, maior, menor))
