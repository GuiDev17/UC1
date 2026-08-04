while True:
    try:
        numero = int(input("Digte um numero inteiro para saber a metade: "))
        metade = numero / 2

        print(f"A metade de {numero} é {metade}")

        break
    
    except ValueError:
        print("Erro: Voce digitou letras, por favor digite um numero inteiro!")