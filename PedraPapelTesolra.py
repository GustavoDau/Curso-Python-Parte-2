from random import randint
itens = ('pedra', 'papel', 'tesolra')
computador = randint(0, 2)
jogador = int(input('''qual vai ser a sua jogada?
0 - pedra
1 - papel
2 - tesolra'''))
print('o computador escolheu {}'.format(itens[computador]))
print('o jogador escolheu {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('empate')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('computador vence')

elif computador == 1:
    if jogador == 0:
        print('computador vence')
    elif jogador == 1:
        print('empate')
    elif jogador == 2:
        print('jogador vence')
elif computador == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('computador vence')
    elif jogador == 2:
        print('empate')