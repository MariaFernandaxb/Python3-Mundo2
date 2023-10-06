# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

total = prodmil = menor = cont = 0
barato = ''

while True: 
    produto = input('Produto:  ')
    preco = float(input('Preço : R$ '))
    cont += 1
    total += preco

    if preco > 1000:
        prodmil += 1 

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar ? [S/N]').strip().upper()[0]
    if resp == 'N':
        break


print('=-'*10, 'FIM DO PROGRAMA', '=-'*10)
print(f'O total da compra foi : R$ {total:.2f}')
print(f'Tem {prodmil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')