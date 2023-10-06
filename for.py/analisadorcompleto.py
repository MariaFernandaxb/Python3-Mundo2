#  Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idade = 0
media_idade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1,5):
    print (f'===={pessoa}ª Pessoa ====')
    nome = input(f'{pessoa}ª : Digite seu nome: ')
    idade = int(input(f'{pessoa}ª: Digite sua idade: '))
    sexo = input(f'{pessoa}ª: Digite o sexo[M/F]: ') .strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm'and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media_idade = soma_idade / 4
print(f'A media de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')