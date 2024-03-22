cont = 0
n = 0
soma = 0
while cont < 5:
    n = float(input("Digite um número real: "))
    if n > 10:
        soma = soma + n
        cont += 1
    else:
        print("Número inválido, informe novamente!")
print(f"Soma = {soma}")