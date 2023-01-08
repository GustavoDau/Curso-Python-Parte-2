#Melhore o DESAFIO de PA, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

n = int(input('Entre com o primeiro termo'))
razao = int(input('entre com a razao'))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' - ')
        termo += razao
        cont += 1
    print('PAUZA')
    mais = int(input("\nquantos termos a mais voce gostaria de acrescentar?"))
print('total de termos foi {}'.format(total))