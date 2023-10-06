from random import randint #biblioteca que gera valores aleatórios. 
from time import sleep
escolha = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2) 
print('''OPÇÕES:
[0] Pedra 
[1] Papel
[2] Tesoura
Escolha uma opção: ''')

jogador = int(input("Qual é sua jogada? "))

print('-='*15)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO !!! ")
print('-='*15)

print(f"JOGADOR JOGOU: {escolha[jogador]}")
print(f"COMPUTADOR JOGOU: {escolha[computador]}")

print('-='*15)
if computador == 0: #pedra
    if jogador == 0:
        print("EMPATE") 
    elif jogador == 1:
         print("JOGADOR VENCE !")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("OPÇÃO INVALIDA. TENTE NOVAMENTE")
elif computador == 1: #papel
    if jogador == 0: 
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("OPÇÃO INVALIDA. TENTE NOVAMENTE")
elif computador == 2: #Tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("OPÇÃO INVALIDA. TENTE NOVAMENTE")