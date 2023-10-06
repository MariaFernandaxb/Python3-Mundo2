# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

#

cont = totH = tot18 = totM20 = 0

while True:
    idade = int(input('Digite a idade : '))
    sexo = ' '
    while sexo not in 'MF':
     sexo = str(input('Masculino ou Feminino ? [F/M] : ')).strip().upper()[0]
    
    if sexo == 'M':
        totH += 1
    
    if idade >= 18:
       tot18 += 1

    if idade > 20 and sexo == 'F':
        totM20 += 1
    
    resp = ' '
    while resp not in 'SN':
       resp = str(input('Quer continuar? : [S/N] : ')).strip().upper()[0]
    if resp == 'N':
        break
       
print(f'Total de pessoas com maior de 18 anos = {tot18}')
print(f'Total de mulheres com idade menor que 20 = {totM20}')
print(f'Total de homens cadastrados = {totH}')

    


