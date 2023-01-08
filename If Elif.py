#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano = int(input('informe o ano de nascimento'))
idade = atual - ano
alistamento = 18 - idade
if idade < 18:
    alistamento = 18 - idade
    print('voce ainda pode se alistar pois falta {} anos pro tempo limite'.format(alistamento))
elif idade ==18:
    print('voce tem q se alistar imediatamente')
else:
    alistamento = idade - 18
    print('voce nao pode se alistar mais pois passou {} anos do tempo limite'.format(alistamento))

#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto / à vista no cartão: 5% de desconto / em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

preco = float(input('entre com o valor do produto'))
opcao = int(input('''digite a opcao desejada:
1 - A vista em dinheiro cheque
2 - a vista no cartao
3 - em 2x no cartao
4 - 3x ou mais no cartao'''))
if opcao == 1:
    valor = preco - (preco * 0.1)
    print(f'o preco normal a ser pagado eh de {preco:.2f} e com o desconto sera de {valor:.2f}')
elif opcao == 2:
    valor = preco - (preco * 0.05)
    print(f'o preco normal a ser pagado eh de {preco:.2f} e com o desconto sera de {valor:.2f}')
elif opcao == 3:
    print(f'o preco normal a ser pagado eh de {preco:.2f}')
elif opcao == 4:
    valor = preco + (preco * 0.2)
    totparc = int(input('em quantas parcelas voce quer sua compra?'))
    parcela = valor / totparc
    print(f'o preco da parcela a ser pagada eh de {parcela:.2f} e com os juros o valor total sera de {valor:.2f}')
else:
    print('numero digitado incoreto, tente novamente')