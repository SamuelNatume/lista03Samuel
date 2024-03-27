soma = 0
contador = 0
while contador < 10:
    print("Digite uma nota", end="")
    nota = float(input(": "))
    soma = soma + nota
    contador = contador + 1
media = soma/contador
print(f"Essa é a sua média: {media:.2f}")
