#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número: "))
escolha = int(input("1) Binário 2)Octal 3)Hexadecimal: "))

if escolha == 1:
    print(f"O numero {numero} em Binário fica: {bin(numero)[2:]}")# bin transformando numero em binário
elif escolha == 2:
     print(f"O numero {numero} em Octal fica: {oct(numero)[2:]}") #oct transforma o numero em octal
elif escolha == 3:
    print(f"O numero {numero} em Hexadecimal fica: {hex(numero)[2:]}") #hex transforma o numero em Hexadecimal
else: 
    print("Opção inválida! Tente novamente.")