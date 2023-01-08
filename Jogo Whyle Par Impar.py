#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
vitorias = 0
while True:
    jogador = int(input('Digite um numero'))
    computador = randint(0, 11)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('voce quer par ou impar')).strip().upper()[0]
    print(f'voce jogou {jogador} e o computador jogou {computador} e o total foi de {total}')
    print('deu PAR'if total % 2 == 0 else 'deu IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('voce venceu')
            vitorias +=1
        else:
            print('voce perdeu')
            break
    if escolha =='I':
        if total % 2 == 1:
            print('voce venceu')
            vitorias += 1
        else:
            print('voce perdeu')
            break
print(f'voce venceu {vitorias} partidas')