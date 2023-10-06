# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# EXEMPLO : APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = input("Digite uma frase: ").strip() .upper() #sprit = elimar espaços e  upper= colocando em maiúscula
palavras = frase.split() #split = separado em lista
junto = ''.join(palavras) #join = juntar 
inverso = ''
for letra in range(len(junto)-1, -1, -1): # inverso
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')


#metodo otimizado sem o for 

# frase = input("Digite uma frase: ").strip() .upper() #sprit = elimar espaços e  upper= colocando em maiúscula
# palavras = frase.split() #split = separado em lista
# junto = ''.join(palavras) #join = juntar 
# inverso = ''
# inverso = junto[::-1]
# print(f'O inverso de {junto} é {inverso}')
# if inverso == junto:
#     print('Temos um palíndromo')
# else: 
#     print('A frase não é um palíndromo')


