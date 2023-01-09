#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
#a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues

valor = int(input('Digite o valor que voce quer sacar'))
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break
