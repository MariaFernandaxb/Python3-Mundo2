# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

r1= float(input("Digite o primeiro lado: "))
r2= float(input("Digite o segundo lado: "))
r3 = float(input("Digite o terceiro lado: "))
# total = lado1 + lado2 + lado3

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os seguimentos acima podem formar um triângulo:", end= '')
    if r1 == r2 == r3: # condição alinhada
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
 print("Os seguimentos acima não podem formar um triângulo")
