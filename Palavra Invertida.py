#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print('temos um palindromo')
else:
    print('a frase n eh uma palindromo')