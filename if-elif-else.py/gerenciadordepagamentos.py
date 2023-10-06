# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros
print('=='*10,"BOA COMPRA",'=='*10)
valor_produto = float(input("Digite o valor do produto: R$ "))
pagamento = int(input(''' FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto 
[3] em até 2x no cartão: preço formal 
[4] 3x ou mais no cartão: 20% de juros
Qual a condição de pagamento: '''))

if pagamento == 1:
   condição = valor_produto - (valor_produto * 10 / 100) 

elif pagamento == 2:
   condição = valor_produto - (valor_produto * 5 / 100)

elif pagamento == 3:
     condição = valor_produto / 2
     print(f"Em 2x no cartão sem juros, cada parcela fica {condição}")
elif pagamento == 4:
    parcelas = int(input("Quantas parcelas? : "))
    condição = valor_produto + (valor_produto * 20/100)
    total = condição / parcelas
    print(f"Em {parcelas}x no cartão cada parcela fica {total:.2f}")
else: 
    condição = 0
    print("Opção inválida. Tente novamente")

print(f"O valor do produto é de R${valor_produto}, sua compra sairá por: R$ {condição}")