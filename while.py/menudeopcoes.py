#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
opcao = 0
while opcao != 5:
    sleep(1)
    print('''Menu de Opções:
        [1]Somar
        [2]Multiplicar
        [3]Maior
        [4]Novos Numeros
        [5]Sair do programa''')
    opcao = int(input('>>>>> Qual a sua opção ? '))
    if opcao == 1 :
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} = {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'A multiplicação entre {n1} * {n2} ={ produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print(f'O maior produto é {maior}')
        else:
            maior = n2
            print(f'O maior produto é {maior}')
    elif opcao == 4:
        print('Digite os novos números: ')
        n1 = int(input('1ª número: '))
        n2 = int(input('2º número: '))
    elif opcao == 5:
        print('Finalizando o menu')
        sleep(1)
        print('Até a próxima !')
    else:
        print('Opção inválida ! Tente novamente. ')
    print('*='*10)
   
print('Fim do programa')


      
      
