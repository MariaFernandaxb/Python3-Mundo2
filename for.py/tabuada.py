#  Refaça o DESAFIO 9 (python mundo1), mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Qual número você deseja para a tabuada? : '))
for n in range (1,11):
    print (f'{numero} x {n:2} = {n*numero}')
