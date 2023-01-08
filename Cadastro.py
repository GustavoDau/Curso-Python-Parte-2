#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
#grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

maior = 0
nomevelho = 0
soma = 0
cont = 0
for c in range(1, 5):
    nome = str(input('Digite o nome'))
    idade = int(input('Digite a idade'))
    sexo = str(input('digite o sexo M ou F')).upper()
    soma += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        cont += 1
media = soma/4
print('a media de idade do hrupo eh {} anos'.format(media))
print('o homem mais velho tem {} anos e se chama {}'.format(maior, nomevelho))
print('ao todo sao {} mulheres com menos de 20 anos'.format(cont))
