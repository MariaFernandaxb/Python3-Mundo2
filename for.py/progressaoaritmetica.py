# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('='*10, 'Progressão Aritmética', '='*10)

p_termo = int(input("Digite o termo: "))
razao = int(input("Digite a razão: "))
decimo = p_termo + (10-1) * razao

for i in range(p_termo, decimo + razao, razao):
    print(f'{i}', end= ' => ')

print('FIM !')