# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores

resp = 'S'
soma = quant = media = menor = maior = 0
while resp in 'sS':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if  num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
media = soma / quant
print(f'Foram digitados {quant} e a média foi {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')