# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

print('-='*5, 'TABUADA' ,'-='*5)
while True:
    tabuada = int(input('Digite um número para ver a tabuada: '))
    if tabuada <= 0:
        print('PROGRAMA ENCERRADO ! Volte sempre !')
        break
            
    for t in range(1,11):
            print(f'{t} X {tabuada} = {tabuada * t}')            
            

