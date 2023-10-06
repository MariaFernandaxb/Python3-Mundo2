# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Qual o valor da casa ? R$ "))
salario_comprador = float(input("Salário do comprador? R$ "))
anos_pagamento = int(input("Em quantos anos será pago? "))
prestação = valor_casa / (anos_pagamento *12)
minimo = salario_comprador * 30 /100
# print(minimo)
print(f"Para pagar uma casa de R${valor_casa:.2f} em {anos_pagamento} anos \n o valor da prestação será de {prestação:.2f}")

if prestação <= minimo:
    print("Emprestimo CONCEDIDO ")
else: 
    print("Empréstimo NEGADO")