# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número: "))
tot = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\033[33m', end = ' ')
        tot += 1 
    else:
        print('\033[031m', end =' ')
    print(f'{i}', end=' ')

print(f'\n\033[mO numero {n} foi divisel {tot} vezes')

if tot == 2:
    print(f'Então o numero {n} é PRIMO')
else:
    print(f'O número {n} não é PRIMO')