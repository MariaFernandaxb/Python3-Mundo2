#  Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('=-'*10, 'PROGRESSÃO ARITIMÉTICA','=-'*10)
primeiro = int(input('Digite o termo: '))
razao = int(input('Razão da PA: '))
print(f'Esses são os 10 primeiros termos de {primeiro}')
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0 :
    total = total + mais
    while cont <= total:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais ?:  '))
print(f'Foram mostrados {total} termos ')
print('Fim')