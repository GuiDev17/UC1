try:
    numerador = int(input("Digite o numero a ser dividido: "))
    denominador = int(input("Digite o valor da divisao: "))

    res = numerador / denominador
    print(f"O resultado é {res}")

except ValueError:
    print("Digite apenas numeros inteiros")

except ZeroDivisionError:
    print("Nao pode ser divido por 0")