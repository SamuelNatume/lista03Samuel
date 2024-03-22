contpar = 0
contimpar = 0
par = 0
impar = 0
somapar = 0
somaimpar = 0
num = 0
while contpar < 5 and somaimpar <= 30:
    if num >= 0:
        num = int(input("Digite um número inteiro: "))
        if num % 2 == 0:
            par += 1
            somapar += num
            contpar += 1
        elif num % 2 != 0:
            impar += 1
            somaimpar += num
            contimpar += 1
    else:
        num = int(input("Digite outro número inteiro, negativo não conta: "))
print(f"Você digitou {contimpar} números impares e a soma entre eles foi {somaimpar}.")
print(f"Você digitou {contpar} números pares e a soma entre eles foi {somapar}.")
 