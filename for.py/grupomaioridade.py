# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano_atual = date.today().year
tot_menor = 0 #Quantidade pessoas menores de idade
tot_maior = 0 #Quantidade pessoas maior de idade

for pessoa in range(1,8):
    nasc = int(input(f'{pessoa}ª : Digite seu ano de nascimento: '))
    idade = ano_atual - nasc
    if idade >= 21 :
        tot_maior +=1
    else:
        tot_menor += 1 

print(f'São {tot_maior} pessoa(s) maior(es) de idade')
print(f'São {tot_menor} pessoa(s) menor(es) de idade')