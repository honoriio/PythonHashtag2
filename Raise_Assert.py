def soma(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


while True:
    numero = int(input("Digite um numero: "))
    sair = input("Deseja sair? [S/N] ").upper()
    if sair == "S":
        break


print(soma(numero))
