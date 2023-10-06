# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('__'*30)
print('=-'*5 , 'BANCO PROC' , '=-'*5)
saque  =  int(input('Valor para saque R$: '))
print('__'*30)
total = saque
nota = 50
totnota = 0

while True: 
    if total >= nota:
        total -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'Total de {totnota} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if total == 0:
            break

print('__'*30)
print(f'Saque de R${saque} realizado com sucesso ! Volte sempre')
print('__'*30)



