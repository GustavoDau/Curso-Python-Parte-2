#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Entre com o primeiro termo'))
razao = int(input('entre com a razao'))
decimo = n + 10 * razao
for c in range(n, decimo, razao):
    print(c,  end=' ')


